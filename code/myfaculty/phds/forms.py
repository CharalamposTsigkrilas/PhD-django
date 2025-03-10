from django.forms import ModelForm
from .models import JournalPublication, ConferencePublication, Teaching
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML

JOURNAL_FIELDS = ['candidate', 'title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
CONFERENCE_FIELDS = ['candidate', 'title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
TEACHING_FIELDS = ['candidate', 'faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']

PHD_JOURNAL_FIELDS = ['title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
PHD_CONFERENCE_FIELDS = ['title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
PHD_CREATE_TEACHING_FIELDS = ['faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments']
PHD_SPECTATE_TEACHING_FIELDS = ['faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']

# SEC_JOURNAL_FIELDS = ['candidate', 'title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
# SEC_CONFERENCE_FIELDS = ['candidate', 'title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
# SEC_TEACHING_FIELDS = ['candidate', 'faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']

# STAFF_JOURNAL_FIELDS = ['candidate', 'title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
# STAFF_CONFERENCE_FIELDS = ['candidate', 'title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
# STAFF_TEACHING_FIELDS = ['candidate', 'faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']

# PHD_JOURNAL_FIELDS = ['title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
# PHD_CONFERENCE_FIELDS = ['title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
# PHD_TEACHING_FIELDS = ['faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']


LABELS = {
    'candidate' : 'Υποψήφιος Διδάκτορας',
    'title' : 'Τίτλος',
    'authors_list' : 'Λίστα Συγγραφέων',
    'has_supervisor' : 'Ο Επιτηρητής είναι στη λίστα των Συγγραφέων;',
    'journal' : 'Περιοδικό',
    'publisher' : 'Εκδότης',
    'volume' : 'Τόμος',
    'issue' : 'Τεύχος',
    'year' : 'Έτος',
    'doi' : 'Ψηφιακό Αναγνωριστικό (DOI)',
    'conference_name' : 'Όνομα Συνεδρίου',
    'venue' : 'Χώρος Συνεδρίου',
    'faculty' : 'Επιτηρητής Υποψήφιου Διδάκτορα',
    'course' : 'Μάθημα',
    'teaching_type' : 'Είδος Φροντιστηρίου',
    'hours_per_week' : 'Ώρες Διδασκαλίας τη Βδομάδα',
    'no_weeks' : 'Αριθμός Εβδομάδων',
    'have_contract' : 'Έχει Σύμβαση ο Διδάκτορας;',
    'comments' : 'Σχόλια',
    'approved_by_faculty' : 'Έγκριση',
    'approved_date' : 'Ημερομηνία Έγκρισης'
}

PHD_CREATE_JOURNAL_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"
            ),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in PHD_JOURNAL_FIELDS
            ]
        )

SEC_CREATE_JOURNAL_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"
            ),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in JOURNAL_FIELDS
            ]
        )

SEC_EDIT_JOURNAL_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"
            ),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in JOURNAL_FIELDS
            ]
        )
            # Journal
            # Row(
            #     Div(Field('candidate'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('title'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('authors_list'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('has_supervisor'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('journal'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('publisher'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('volume'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('issue'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('year'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('doi'),css_class = 'col-md-12'),
            #     css_class="row"),
            # )

PHD_CREATE_CONFERENCE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in PHD_CONFERENCE_FIELDS
            ]    
        )

SEC_CREATE_CONFERENCE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in CONFERENCE_FIELDS
            ]    
        )

SEC_EDIT_CONFERENCE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in CONFERENCE_FIELDS
            ]    
        )
            # Conference
            # Row(
            #     Div(Field('candidate'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('title'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('authors_list'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('conference_name'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('venue'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('year'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('has_supervisor'),css_class = 'col-md-12'),
            #     css_class="row"),
            # )

PHD_CREATE_TEACHING_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in PHD_CREATE_TEACHING_FIELDS
            ]
        )

SEC_CREATE_TEACHING_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in TEACHING_FIELDS
            ]
        )

SEC_EDIT_TEACHING_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in TEACHING_FIELDS
            ]
        )

STAFF_EDIT_TEACHING_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            *[  
                Row(
                    Div(Field(field), css_class='col-md-12'),
                    css_class="row"
                ) for field in TEACHING_FIELDS
            ]
        )   
            # Teaching
            # Row(
            #     Div(Field('candidate'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('faculty'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('course'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('year'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('teaching_type'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('hours_per_week'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('no_weeks'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('have_contract'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('comments'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('approved_by_faculty'),css_class = 'col-md-12'),
            #     css_class="row"),
            # Row(
            #     Div(Field('approved_date'),css_class = 'col-md-12'),
            #     css_class="row"),
            # )

# Journal Forms 
class PhdCreateJournalForm(ModelForm):

    class Meta:
        fields = PHD_JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = PHD_CREATE_JOURNAL_LAYOUT

class PhdSpectateJournalFormRestricted(ModelForm):

    class Meta:
        fields = PHD_JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in PHD_JOURNAL_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateJournalForm(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_JOURNAL_LAYOUT

class SecEditJournalForm(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_JOURNAL_LAYOUT

class StaffSpectateJournalFormRestricted(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in JOURNAL_FIELDS:
            self.fields[k].disabled = True


# Conference Forms
class PhdCreateConferenceForm(ModelForm):

    class Meta:
        fields = PHD_CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = PHD_CREATE_CONFERENCE_LAYOUT

class PhdSpectateConferenceFormRestricted(ModelForm):

    class Meta:
        fields = PHD_CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in PHD_CONFERENCE_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateConferenceForm(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_CONFERENCE_LAYOUT

class SecEditConferenceForm(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_CONFERENCE_LAYOUT

class StaffSpectateConferenceFormRestricted(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in CONFERENCE_FIELDS:
            self.fields[k].disabled = True


# Teaching Forms
class PhdCreateTeachingForm(ModelForm):

    class Meta:
        fields = PHD_CREATE_TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = PHD_CREATE_TEACHING_LAYOUT

class PhdSpectateTeachingFormRestricted(ModelForm):

    class Meta:
        fields = PHD_SPECTATE_TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in PHD_SPECTATE_TEACHING_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateTeachingForm(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_TEACHING_LAYOUT

class SecEditTeachingForm(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_TEACHING_LAYOUT

class StaffSpectateAcceptRejectTeachingFormRestricted(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in TEACHING_FIELDS:
            if k != 'approved_by_faculty':
                self.fields[k].disabled = True
                
        self.helper = FormHelper()
        self.helper.layout = STAFF_EDIT_TEACHING_LAYOUT