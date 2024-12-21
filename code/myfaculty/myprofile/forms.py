from django import forms
from .models import StaffMember, Associate, Student, PhDStudent
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML

STAFF_FIELDS_DISABLED = ['email', 'given_name', 'surname', 'title']
ASSOCIATE_FIELDS_DISABLED = ['email', 'given_name', 'surname', 'seat_no', 'office_no']
STUDENT_FIELDS_DISABLED = ['email', 'given_name', 'surname', 'program', 'reg_num']

LABELS =  {
            'email' : 'Ε-mail', 
            'given_name' : 'Όνομα', 
            'surname' : 'Επώνυμο', 
            'fathers_name' : 'Όνομα Πατρός', 
            'date_of_birth' : 'Ημερομηνία Γέννησης', 
            'tin' : 'ΑΦΜ', 
            'ssn' : 'ΑΜΚΑ', 
            'institution' : 'Φορεάς', 
            'school' : 'Σχολή', 
            'title' : 'Ιδιότητα',
            'home_address_street' : 'Οδός', 
            'home_address_po_box' : 'Ταχυδρομικός Κώδικας',
            'home_address_city' : 'Πόλη', 
            'home_address_country' : 'Χώρα', 
            'mobile_phone' : 'Κινητό Τηλέφωνο', 
            'home_phone' : 'Τηλέφωνο Οικίας',
            'work_address_street' : 'Οδός', 
            'work_address_po_box' : 'Ταχυδρομικός Κώδικας', 
            'work_address_city' : 'Πόλη', 
            'work_address_country' : 'Χώρα', 
            'work_phone' : 'Τηλέφωνο Εργασίας',
            'seat_no' : 'Αριθμός Θέσης',
            'office_no' : 'Γραφείο',
            'card_no' : 'Αριθμός Κάρτας',
            'program' : 'Πρόγραμμα Σπουδών',
            'reg_num' : 'Αριθμός Μητρώου',
            'is_internal' : 'Είναι εσωτερικός;' 
        }

SEC_STAFF_MEMBER_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Προφίλ </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('surname'),css_class = 'col-md-3'),
                Div(Field('given_name'),css_class = 'col-md-3'),
                Div(Field('fathers_name'),css_class = 'col-md-3'),                
                Div(Field('email'),css_class = 'col-md-3'),                
                css_class="row"),
            Row(
                Div(Field('date_of_birth'),css_class = 'col-md-4'),
                Div(Field('ssn'),css_class = 'col-md-4'),
                Div(Field('tin'),css_class = 'col-md-4'),                
                css_class="row"),
            Row(
                Div(Field('institution'),css_class = 'col-md-4'),
                Div(Field('school'),css_class = 'col-md-4'),
                Div(Field('title'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('is_internal'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                HTML('<p></p><h5> Διεύθυνση Κατοικίας </h5>'),
                css_class="row"
            ),
            Row(
                Div(Field('home_address_street'),css_class = 'col-md-4'),
                Div(Field('home_address_po_box'),css_class = 'col-md-4'),
                Div(Field('home_address_city'),css_class = 'col-md-4'),
                css_class="row"),                                
            Row(
                Div(Field('home_address_country'),css_class = 'col-md-4'),
                Div(Field('mobile_phone'),css_class = 'col-md-4'),
                Div(Field('home_phone'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                HTML('<p></p><h5> Διεύθυνση Εργασίας </h5>'),
                css_class="row"
            ),
            Row(
                Div(Field('work_address_street'),css_class = 'col-md-4'),
                Div(Field('work_address_po_box'),css_class = 'col-md-4'),
                Div(Field('work_address_city'),css_class = 'col-md-4'),
                css_class="row"),                                
            Row(
                Div(Field('work_address_country'),css_class = 'col-md-4'),
                Div(Field('work_phone'),css_class = 'col-md-4'),
                css_class="row"),
            )

STAFF_MEMBER_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Προφίλ </h4>'),css_class = 'col-md-8'),               
               css_class="row"),
            Row(
                Div(Field('surname'),css_class = 'col-md-4'),
                Div(Field('given_name'),css_class = 'col-md-4'),                               
                Div(Field('email'),css_class = 'col-md-4'),                
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-4'),
                css_class="row"),            
            )
ASSOCIATE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Προφίλ </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('surname'),css_class = 'col-md-3'),
                Div(Field('given_name'),css_class = 'col-md-3'),
                Div(Field('fathers_name'),css_class = 'col-md-3'),                
                Div(Field('email'),css_class = 'col-md-3'),                
                css_class="row"),
            Row(
                Div(Field('date_of_birth'),css_class = 'col-md-4'),
                Div(Field('ssn'),css_class = 'col-md-4'),
                Div(Field('tin'),css_class = 'col-md-4'),                
                css_class="row"),
            Row(
               Div(HTML('<p></p><h5> Θέση Εργασίας </h5>'),css_class = 'col-md-8'),
               css_class="row"),
            Row(
               Div(Field('seat_no'),css_class = 'col-md-4'),
               Div(Field('office_no'),css_class = 'col-md-4'),                
               css_class="row"),
            Row(
                HTML('<p></p><h5> Διεύθυνση Κατοικίας </h5>'),
                css_class="row"
            ),
            Row(
                Div(Field('home_address_street'),css_class = 'col-md-4'),
                Div(Field('home_address_po_box'),css_class = 'col-md-4'),
                Div(Field('home_address_city'),css_class = 'col-md-4'),
                css_class="row"),                                
            Row(
                Div(Field('home_address_country'),css_class = 'col-md-4'),
                Div(Field('mobile_phone'),css_class = 'col-md-4'),
                Div(Field('home_phone'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('work_phone'),css_class = 'col-md-4'),
                css_class="row"),
            )

SEC_ASSOCIATE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Προφίλ </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('surname'),css_class = 'col-md-4'),
                Div(Field('given_name'),css_class = 'col-md-4'),
                Div(Field('fathers_name'),css_class = 'col-md-4'),                
                css_class="row"),
            Row(
                Div(Field('email'),css_class = 'col-md-3'),
                Div(Field('date_of_birth'),css_class = 'col-md-3'),
                Div(Field('ssn'),css_class = 'col-md-3'),
                Div(Field('tin'),css_class = 'col-md-3'),                
                css_class="row"),
            Row(
               Div(HTML('<p></p><h5> Θέση Εργασίας </h5>'),css_class = 'col-md-8'),
               css_class="row"),
            Row(
               Div(Field('seat_no'),css_class = 'col-md-4'),
               Div(Field('office_no'),css_class = 'col-md-4'),                
               Div(Field('card_no'),css_class = 'col-md-4'),                
               css_class="row"),
            Row(
                HTML('<p></p><h5> Διεύθυνση Κατοικίας </h5>'),
                css_class="row"
            ),
            Row(
                Div(Field('home_address_street'),css_class = 'col-md-4'),
                Div(Field('home_address_po_box'),css_class = 'col-md-4'),
                Div(Field('home_address_city'),css_class = 'col-md-4'),
                css_class="row"),                                
            Row(
                Div(Field('home_address_country'),css_class = 'col-md-4'),
                Div(Field('mobile_phone'),css_class = 'col-md-4'),
                Div(Field('home_phone'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('work_phone'),css_class = 'col-md-4'),
                css_class="row"),
            )

class StaffForm(ModelForm):

    class Meta:

        model = StaffMember

        fields = ['email', 'given_name', 'surname', 'fathers_name', 'date_of_birth', 'tin', 'ssn', 'institution', 'school', 'title', 
                  'home_address_street', 'home_address_po_box', 'home_address_city', 'home_address_country', 'mobile_phone', 'home_phone',
                  'work_address_street', 'work_address_po_box', 'work_address_city', 'work_address_country', 'work_phone', 'is_internal']
        
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = SEC_STAFF_MEMBER_LAYOUT

class AssociateForm(ModelForm):

    class Meta:
         
         model = Associate

         fields = ['email', 'given_name', 'surname', 'fathers_name', 'date_of_birth', 'tin', 'ssn', 'card_no',  
                  'home_address_street', 'home_address_po_box', 'home_address_city', 'home_address_country', 'mobile_phone', 'home_phone',
                  'work_phone', 'seat_no', 'office_no']
         
         labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_ASSOCIATE_LAYOUT

class AssociateFormRestricted(AssociateForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in ASSOCIATE_FIELDS_DISABLED:
            self.fields[k].disabled = True

        self.helper = FormHelper()
        self.helper.layout = ASSOCIATE_LAYOUT
             
class StaffFormRestricted(StaffForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in STAFF_FIELDS_DISABLED:
            self.fields[k].disabled = True

        self.helper = FormHelper()
        self.helper.layout = STAFF_MEMBER_LAYOUT
         
class StudentFormRestricted(ModelForm):

    class Meta:
        fields = STUDENT_FIELDS_DISABLED
        model = Student
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in STUDENT_FIELDS_DISABLED:
            self.fields[k].disabled = True

# Demo form for PhD Students - It will be changed in the future
class PhDStudentForm(forms.ModelForm):
    class Meta:
        model = PhDStudent
        fields = '__all__'
        labels = {
            'id_number': 'ID Number',
            'email': 'Email',
            'given_name': 'Given Name',
            'surname': 'Surname',
            'fathers_name': "Father's Name",
            'date_of_birth': 'Date of Birth',
            'external_email': 'External Email',
            'gender': 'Gender',
            'mobile_phone': 'Mobile Phone',
            'home_phone': 'Home Phone',
            'home_address': 'Home Address',
            'subject_gr': 'Subject (Greek)',
            'subject_en': 'Subject (English)',
            'inscription_date': 'Inscription Date',
            'inscription_ref': 'Inscription Reference',
            'photo': 'Photo',
            'cv_gr': 'CV (Greek)',
            'cv_en': 'CV (English)',
            'scopus_id': 'Scopus ID',
        }
        widgets = {
            'id_number': forms.TextInput(attrs={'placeholder': 'e.g. 12345678', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e.g. example@example.com', 'class': 'form-control'}),
            'given_name': forms.TextInput(attrs={'placeholder': 'e.g. John', 'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'placeholder': 'e.g. Doe', 'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'placeholder': 'e.g. Michael', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'e.g. 1990-01-01', 'class': 'form-control', 'type': 'date'}),
            'external_email': forms.EmailInput(attrs={'placeholder': 'e.g. external@example.com', 'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'placeholder': 'e.g. Male/Female', 'class': 'form-control'}),
            'mobile_phone': forms.TextInput(attrs={'placeholder': 'e.g. +123456789', 'class': 'form-control'}),
            'home_phone': forms.TextInput(attrs={'placeholder': 'e.g. +123456789', 'class': 'form-control'}),
            'home_address': forms.TextInput(attrs={'placeholder': 'e.g. 123 Main St', 'class': 'form-control'}),
            'subject_gr': forms.TextInput(attrs={'placeholder': 'e.g. Πληροφορική', 'class': 'form-control'}),
            'subject_en': forms.TextInput(attrs={'placeholder': 'e.g. Computer Science', 'class': 'form-control'}),
            'inscription_date': forms.DateInput(attrs={'placeholder': 'e.g. 2023-09-01', 'class': 'form-control', 'type': 'date'}),
            'inscription_ref': forms.TextInput(attrs={'placeholder': 'e.g. Ref123', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'cv_gr': forms.Textarea(attrs={'placeholder': 'Εισάγετε το βιογραφικό στα Ελληνικά', 'class': 'form-control', 'rows': 4}),
            'cv_en': forms.Textarea(attrs={'placeholder': 'Enter the CV in English', 'class': 'form-control', 'rows': 4}),
            'scopus_id': forms.TextInput(attrs={'placeholder': 'e.g. 12345678', 'class': 'form-control'}),
        }

