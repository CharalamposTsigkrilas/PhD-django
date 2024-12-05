from .models import Thesis
from myprofile.models import StaffMember
from django.shortcuts import get_object_or_404
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML
from django.core.exceptions import ValidationError
from dal import autocomplete
from myprofile.models import Student
from datetime import datetime

def sanitize_fields(fields):
    return_fields = []
    
    for f in fields:
        if f[-1] == '*' or f[-1] == '-':
            return_fields.append(f[:-1])
        else:
            return_fields.append(f)
    return return_fields

FIELDS = ['title_gr', 'title_en', 'abstract','offered_in', 'is_offered', 'supervisor', 'member1', 'member2', 'created_date', 'updated_date']

SEC_EDIT_FIELDS = ['title_gr', 'title_en', 'abstract','offered_in', 'is_offered', 'supervisor', 'member1', 'member2', 'assigned_to_char', 
                   'grade_sup', 'grade_member1', 'grade_member2', 'assignment_date-', 'assignment_ga']

SEC_CREATE_FIELDS = ['title_gr', 'title_en', 'abstract','offered_in', 'is_offered', 'supervisor', 'member1', 'member2', 'assigned_to_char']

STAFF_EDIT_FIELDS = ['title_gr*', 'title_en*', 'abstract*','offered_in*', 'is_offered*', 'assigned_to_char', 'member1*', 'member2*', 
                     'grade_sup-', 'grade_member1-', 'grade_member2-', 'assignment_date-', 'assignment_ga-']

STAFF_CREATE_FIELDS = ['title_gr*', 'title_en*', 'abstract*','offered_in*', 'is_offered*', 'member1*', 'member2*']

PUBLIC_FIELDS = ['title_gr-', 'title_en-', 'abstract-','offered_in-', 'supervisor-', 'member1-', 'member2-']

WIDGET = {
            "supervisor" : autocomplete.ModelSelect2(url='myprofile:staffmember-autocomplete'),
            "member1" : autocomplete.ModelSelect2(url='myprofile:staffmember-autocomplete'),
            "member2" : autocomplete.ModelSelect2(url='myprofile:staffmember-autocomplete'), 
            "assigned_to_char" : autocomplete.ListSelect2(url='myprofile:student-autocomplete')
         }

RANGE_ERROR_MESSAGE = 'Η βαθμολογία πρέπει να είναι ακέραιος αριθμός από 1 εώς 10'

LABELS ={'title_gr' : 'Τίτλος (Ελληνικά)',
         'title_en' : 'Τίτλος (Αγγλικά)',
         'abstract' : 'Περιγραφή',
         'supervisor' : 'Επιβλέπων',
         'member1' : '2ο Μέλος Επιτροπής',
         'member2' : '3ο Μέλος Επιτροπής',
         'updated_date' : 'Ημερομηνία τελευταίας ενημέρωσης', 
         'offered_in' : 'Προσφέρεται σε:',
         'is_offered' : 'Είναι ενεργό;',
         'created_date' : 'Ημερομηνία δημιουργίας',
         'assigned_to_char' : 'Νέα/Αλλαγή Ανάθεσης',
         'grade_sup' : 'Βαθμός Επιβλέποντα',
         'grade_member1' : 'Βαθμός 2ου μέλους επιτροπής',
         'grade_member2' : 'Βαθμός 3ου μέλους επιτροπής',
         'assignment_date' : 'Ημερομηνία καταχώρισης ανάθεσης',  
         'assignment_ga' : 'Συνέλευση Σχολής που έγινε η ανάθεση',         
         }

def build_form_layout(fields):
    layout = Layout(Row(Div(HTML('<h4> Στοιχεία Εργασίας </h4>'),css_class = 'col-lg-8'),
                        Div(Submit('submit', 'Ενημέρωση'),css_class='col-lg-4 text-end'),
                        css_class="row"))
    
    for field in sanitize_fields(fields):
        layout.append(Row(Div(Field(field), css_class="row")))
        
        
    return layout

def build_public_layout(fields):
    layout = Layout(Row(Div(HTML('<h4> Στοιχεία Εργασίας </h4>'),css_class = 'col-lg-8'),                        
                        css_class="row"))
    
    for field in sanitize_fields(fields):
        layout.append(
            Row(
                Div(Field(field), css_class="row")
            )
        )
    return layout

def adjust_fields(form):
    for f in form.Meta.efields:
        # print(f)
        if f[-1] == '*':
            field = f[:-1]
            form.fields[field].required=True
            form.fields[field].disabled=False
            
        elif f[-1] == '-':
            field = f[:-1]
            form.fields[field].required=False
            form.fields[field].disabled=True

class SecCreateForm(ModelForm):

    class Meta:

        model = Thesis
        fields = sanitize_fields(SEC_CREATE_FIELDS)
        labels = LABELS
        efields = SEC_CREATE_FIELDS
        widgets = WIDGET
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adjust_fields(self)
        self.helper = FormHelper()
        self.helper.layout = build_form_layout(SEC_CREATE_FIELDS)

class SecUpdateForm(ModelForm):

    class Meta:

        model = Thesis
        fields = sanitize_fields(SEC_EDIT_FIELDS)
        labels = LABELS
        efields = SEC_EDIT_FIELDS 
        widgets = WIDGET

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adjust_fields(self)
        self.helper = FormHelper()
        self.helper.layout = build_form_layout(self.fields)

    def check_grade_range(self, field):
        if field in self.cleaned_data:
            
            g = self.cleaned_data[field]
            if g:
                if (g<1) or (g>10):               
                    self.add_error(field, RANGE_ERROR_MESSAGE)

    def clean(self):
        super().clean()
        self.check_grade_range('grade_sup')
        self.check_grade_range('grade_member1')
        self.check_grade_range('grade_member2')

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs, commit=False)
        if instance.assigned_to_char:
            instance.assigned_to = Student.objects.get_profile(instance.assigned_to_char)
        
        if 'assigned_to_char' in self.changed_data:
            if self.cleaned_data['assigned_to_char']: 
                self.instance.assignment_date = datetime.now()
            else:
                self.instance.assignment_date = None

        instance.save()
        self.save_m2m()

        return instance

class StaffCreateForm(ModelForm):

    class Meta:

        model = Thesis
        fields = sanitize_fields(STAFF_CREATE_FIELDS)
        labels = LABELS
        efields = STAFF_CREATE_FIELDS
        widgets = WIDGET

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adjust_fields(self)
        self.helper = FormHelper()
        self.helper.layout = build_form_layout(STAFF_CREATE_FIELDS)


class StaffUpdateForm(ModelForm):

    class Meta:

        model = Thesis
        fields = sanitize_fields(STAFF_EDIT_FIELDS)
        labels = LABELS
        efields = STAFF_EDIT_FIELDS
        widgets = WIDGET
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adjust_fields(self)
        self.helper = FormHelper()
        self.helper.layout = build_form_layout(self.fields)
        
    def check_grade_range(self, field):
        if field in self.cleaned_data:
            
            g = self.cleaned_data[field]
            if g:
                if (g<1) or (g>10):               
                    self.add_error(field, RANGE_ERROR_MESSAGE)

    def clean(self):
        super().clean()
        self.check_grade_range('grade_sup')
        self.check_grade_range('grade_member1')
        self.check_grade_range('grade_member2')
        
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs, commit=False)
        if instance.assigned_to_char:
            instance.assigned_to = Student.objects.get_profile(instance.assigned_to_char)

        if 'assigned_to_char' in self.changed_data:
            if self.cleaned_data['assigned_to_char']: 
                self.instance.assignment_date = datetime.now()
            else:
                self.instance.assignment_date = None

        instance.save()
        self.save_m2m()
        return instance


class PublicDetailForm(ModelForm):

    class Meta:

        model = Thesis
        fields = sanitize_fields(PUBLIC_FIELDS)
        labels = LABELS
        efields = PUBLIC_FIELDS
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        adjust_fields(self)
        self.helper = FormHelper()
        self.helper.layout = build_public_layout(PUBLIC_FIELDS)
