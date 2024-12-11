from django import forms
from .models import PhDStudent

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
