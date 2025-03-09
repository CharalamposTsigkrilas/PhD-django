from django.forms import ModelForm
from .models import JournalPublication, ConferencePublication, Teaching
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML

JOURNAL_FIELDS = ['candidate', 'title', 'authors_list', 'has_supervisor', 'journal', 'publisher', 'volume', 'issue', 'year', 'doi']
CONFERENCE_FIELDS = ['candidate', 'title', 'authors_list', 'conference_name', 'venue', 'year', 'has_supervisor']
TEACHING_FIELDS = ['candidate', 'faculty', 'course', 'year', 'teaching_type', 'hours_per_week', 'no_weeks', 'have_contract', 'comments', 'approved_by_faculty', 'approved_date']

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

SEC_JOURNAL_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Περιοδικού </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('authors_list'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('journal'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('publisher'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('volume'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('issue'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('year'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('doi'),css_class = 'col-md-12'),
                css_class="row"),
            )

SEC_CONFERENCE_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Δημοσίευσης Συνεδρίου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('title'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('authors_list'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('conference_name'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('venue'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('year'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('has_supervisor'),css_class = 'col-md-12'),
                css_class="row"),
            )

SEC_TEACHING_LAYOUT = Layout(
            Row(
               Div(HTML('<h4> Στοιχεία Επικουρικού Έργου </h4>'),css_class = 'col-md-8'),
               Div(Submit('submit', 'Ενημέρωση'),css_class='col-md-4 text-end'),
               css_class="row"),
            Row(
                Div(Field('candidate'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('faculty'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('course'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('year'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('teaching_type'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('hours_per_week'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('no_weeks'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('have_contract'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('comments'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_by_faculty'),css_class = 'col-md-12'),
                css_class="row"),
            Row(
                Div(Field('approved_date'),css_class = 'col-md-12'),
                css_class="row"),
            )


class JournalForm(ModelForm):

    class Meta:
        fields = JOURNAL_FIELDS
        model = JournalPublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_JOURNAL_LAYOUT

class JournalFormRestricted(JournalForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in JOURNAL_FIELDS:
            self.fields[k].disabled = True


class ConferenceForm(ModelForm):

    class Meta:
        fields = CONFERENCE_FIELDS
        model = ConferencePublication
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_CONFERENCE_LAYOUT

class ConferenceFormRestricted(ConferenceForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in CONFERENCE_FIELDS:
            self.fields[k].disabled = True


class TeachingForm(ModelForm):

    class Meta:
        fields = TEACHING_FIELDS
        model = Teaching
        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = SEC_TEACHING_LAYOUT

class TeachingFormRestricted(TeachingForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k in TEACHING_FIELDS:
            self.fields[k].disabled = True