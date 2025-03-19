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


# Journal Layouts

PHD_CREATE_JOURNAL_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-6'),                
                Div(Field('authors_list'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-6'),
                Div(Field('publisher'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-4'),
                Div(Field('issue'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-6'),
                Div(Field('doi'),css_class = 'col-md-6'),
                css_class="row"),
            )

PHD_SPECTATE_JOURNAL_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-6'),                
                Div(Field('authors_list'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-6'),
                Div(Field('publisher'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-4'),
                Div(Field('issue'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-6'),
                Div(Field('doi'),css_class = 'col-md-6'),
                css_class="row"),
            )

SEC_CREATE_JOURNAL_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-6'),                
                Div(Field('authors_list'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-6'),
                Div(Field('publisher'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-4'),
                Div(Field('issue'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-6'),
                Div(Field('doi'),css_class = 'col-md-6'),
                css_class="row"),
            )

SEC_EDIT_JOURNAL_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-6'),                
                Div(Field('authors_list'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-6'),
                Div(Field('publisher'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-4'),
                Div(Field('issue'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-6'),
                Div(Field('doi'),css_class = 'col-md-6'),
                css_class="row"),
            )

STAFF_SPECTATE_JOURNAL_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-6'),                
                Div(Field('authors_list'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-6'),
                Div(Field('publisher'),css_class = 'col-md-6'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-4'),
                Div(Field('issue'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-6'),
                Div(Field('doi'),css_class = 'col-md-6'),
                css_class="row"),
            )


# Conference Layouts

PHD_CREATE_CONFERENCE_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'), css_class='col-md-8'),
                Div(Submit('submit', 'Δημιουργία'), css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('title'), css_class='col-md-6'),
                Div(Field('authors_list'), css_class='col-md-6'),
                css_class="row"),
            Row(
                Div(Field('conference_name'), css_class='col-md-4'),
                Div(Field('venue'), css_class='col-md-4'),
                Div(Field('year'), css_class='col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'), css_class='col-md-4'),
                css_class="row"),
            )

PHD_SPECTATE_CONFERENCE_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('title'), css_class='col-md-6'),
                Div(Field('authors_list'), css_class='col-md-6'),
                css_class="row"),
            Row(
                Div(Field('conference_name'), css_class='col-md-4'),
                Div(Field('venue'), css_class='col-md-4'),
                Div(Field('year'), css_class='col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'), css_class='col-md-4'),
                css_class="row"),
            )

SEC_CREATE_CONFERENCE_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'), css_class='col-md-6'),
                Div(Field('authors_list'), css_class='col-md-6'),
                css_class="row"),
            Row(
                Div(Field('conference_name'), css_class='col-md-4'),
                Div(Field('venue'), css_class='col-md-4'),
                Div(Field('year'), css_class='col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'), css_class='col-md-4'),
                css_class="row"),
            )

SEC_EDIT_CONFERENCE_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'), css_class='col-md-6'),
                Div(Field('authors_list'), css_class='col-md-6'),
                css_class="row"),
            Row(
                Div(Field('conference_name'), css_class='col-md-4'),
                Div(Field('venue'), css_class='col-md-4'),
                Div(Field('year'), css_class='col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'), css_class='col-md-4'),
                css_class="row"),
            )

STAFF_SPECTATE_CONFERENCE_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('title'), css_class='col-md-6'),
                Div(Field('authors_list'), css_class='col-md-6'),
                css_class="row"),
            Row(
                Div(Field('conference_name'), css_class='col-md-4'),
                Div(Field('venue'), css_class='col-md-4'),
                Div(Field('year'), css_class='col-md-4'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'), css_class='col-md-4'),
                css_class="row"),
            )


# Teaching Layouts

PHD_CREATE_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('faculty'),css_class = 'col-md-4'),
                Div(Field('course'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            )

PHD_SPECTATE_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('faculty'),css_class = 'col-md-4'),
                Div(Field('course'),css_class = 'col-md-4'),
                Div(Field('year'),css_class = 'col-md-4'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-6'),
                Div(Field('approved_date'),css_class = 'col-md-6'),
                css_class="row"),
            )

SEC_CREATE_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Δημιουργία'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-3'),
                Div(Field('faculty'),css_class = 'col-md-3'),
                Div(Field('course'),css_class = 'col-md-3'),
                Div(Field('year'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-6'),
                Div(Field('approved_date'),css_class = 'col-md-6'),
                css_class="row"),
            )

SEC_EDIT_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-3'),
                Div(Field('faculty'),css_class = 'col-md-3'),
                Div(Field('course'),css_class = 'col-md-3'),
                Div(Field('year'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-6'),
                Div(Field('approved_date'),css_class = 'col-md-6'),
                css_class="row"),
            )

STAFF_SPECTATE_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-3'),
                Div(Field('faculty'),css_class = 'col-md-3'),
                Div(Field('course'),css_class = 'col-md-3'),
                Div(Field('year'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-6'),
                Div(Field('approved_date'),css_class = 'col-md-6'),
                css_class="row"),
            )

STAFF_EDIT_TEACHING_LAYOUT = Layout(
            Row(
                Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
                Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
                css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-3'),
                Div(Field('faculty'),css_class = 'col-md-3'),
                Div(Field('course'),css_class = 'col-md-3'),
                Div(Field('year'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-3'),
                Div(Field('hours_per_week'),css_class = 'col-md-3'),
                Div(Field('no_weeks'),css_class = 'col-md-3'),
                Div(Field('have_contract'),css_class = 'col-md-3'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-6'),
                Div(Field('approved_date'),css_class = 'col-md-6'),
                css_class="row"),
            )

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

        self.helper = FormHelper()
        self.helper.layout = PHD_SPECTATE_JOURNAL_LAYOUT

        for k in PHD_JOURNAL_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateJournalForm(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("candidate", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_JOURNAL_LAYOUT

        self.fields["candidate"].disabled = True  
        if candidate:  
            self.fields["candidate"].initial = candidate

class SecEditJournalForm(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_JOURNAL_LAYOUT

        self.fields["candidate"].disabled = True

class StaffSpectateJournalFormRestricted(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = STAFF_SPECTATE_JOURNAL_LAYOUT

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

        self.helper = FormHelper()
        self.helper.layout = PHD_SPECTATE_CONFERENCE_LAYOUT

        for k in PHD_CONFERENCE_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateConferenceForm(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("candidate", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_CONFERENCE_LAYOUT

        self.fields["candidate"].disabled = True  
        if candidate:  
            self.fields["candidate"].initial = candidate

class SecEditConferenceForm(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_CONFERENCE_LAYOUT
        self.fields["candidate"].disabled = True

class StaffSpectateConferenceFormRestricted(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = STAFF_SPECTATE_CONFERENCE_LAYOUT

        for k in CONFERENCE_FIELDS:
            self.fields[k].disabled = True


# Teaching Forms
class PhdCreateTeachingForm(ModelForm):

    class Meta:
        fields = PHD_CREATE_TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("candidate", None)
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = PHD_CREATE_TEACHING_LAYOUT

        self.fields["faculty"].disabled = True  
        if candidate.supervisor:  
            self.fields["faculty"].initial = candidate.supervisor

class PhdSpectateTeachingFormRestricted(ModelForm):

    class Meta:
        fields = PHD_SPECTATE_TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = PHD_SPECTATE_TEACHING_LAYOUT

        for k in PHD_SPECTATE_TEACHING_FIELDS:
            self.fields[k].disabled = True
        
class SecCreateTeachingForm(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("candidate", None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CREATE_TEACHING_LAYOUT

        self.fields["candidate"].disabled = True  
        self.fields["faculty"].disabled = True
        self.fields["approved_date"].disabled = True

        if candidate:  
            self.fields["candidate"].initial = candidate
        if candidate.supervisor:
            self.fields["faculty"].initial = candidate.supervisor

class SecEditTeachingForm(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_EDIT_TEACHING_LAYOUT

        self.fields["candidate"].disabled = True
        self.fields["faculty"].disabled = True
        self.fields["approved_date"].disabled = True

class StaffSpectateAcceptRejectTeachingFormRestricted(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        for k in TEACHING_FIELDS:            
            self.fields[k].disabled = True

        if self.instance.faculty:
            self.helper = FormHelper()

            if self.instance.faculty.user == self.user and self.instance.approved_by_faculty == False:
                self.fields["approved_by_faculty"].disabled = False
                self.helper.layout = STAFF_EDIT_TEACHING_LAYOUT

            else:    
                self.helper.layout = STAFF_SPECTATE_TEACHING_LAYOUT
                           