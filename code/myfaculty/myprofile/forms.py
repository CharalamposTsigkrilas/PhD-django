from django import forms
from .models import StaffMember, Associate, Student
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



