from django.db import models
from myprofile.models import StaffMember, PhdStudent
from curricula.models import Course
from datetime import date, datetime
from jinja2 import Template
from django.conf import settings
from mailer.auth.gmail import notify  # In production "mailer.auth.gmail" should be changed to "mailer.gmail"

# Create your models here.

class JournalPublication(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField(null=True)
    authors_list = models.TextField(null=True)
    has_supervisor = models.BooleanField(null=True)
    journal = models.CharField(null=True)
    publisher = models.CharField(null=True)
    volume = models.CharField(null=True)
    issue = models.CharField(null=True)
    year = models.IntegerField(null=True)
    doi = models.CharField(null=True)

    def __str__(self):
        return self.title

class ConferencePublication(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField(null=True)
    authors_list = models.TextField(null=True)	
    conference_name = models.CharField(null=True)	
    venue = models.CharField(null=True)
    year = models.IntegerField(null=True)
    has_supervisor = models.BooleanField(null=True)

    def __str__(self):
        return self.title


TEACHING_CREATION_NOTIFICATION = """
Γειά σας! 

Κατατέθηκε ένα νέο Επικουρικό Έργο που αφορά τον/την υποψήφιο/ια Διδάκτορα:
{{ p.candidate }} και απαιτεί έλεγχο.

Συνδεθείτε στην πλατφόρμα για περισσότερες λεπτομέρειες:

"""

TEACHING_APPROVED_NOTIFICATION = """
Γειά σας! 

Το Επικουρικό Έργο σας στο μάθημα "{{ p.course }}", 
και τύπου διδασκαλίας "{{ p.teaching_type }}", 
εγκρίθηκε.

Συνδεθείτε στην πλατφόρμα για περισσότερες λεπτομέρειες:

"""

TEACHING_REJECTED_NOTIFICATION = """
Γειά σας! 

Το Επικουρικό Έργο σας στο μάθημα "{{ p.course }}", 
και τύπου διδασκαλίας "{{ p.teaching_type }}", 
απορρίφθηκε.

Συνδεθείτε στην πλατφόρμα για περισσότερες λεπτομέρειες:

"""

class Teaching(models.Model):

    THEORY_LECTURE = "Theory Lecture"
    LABORATORY_COURSE = "Laboratory Course"
    ASSIGNMENT_CORRECTION = "Assignment Correction"
    TUTORIAL_COURSE = "Tutorial Course"

    TEACHING_TYPES = [
        (THEORY_LECTURE, "Διάλεξη Θεωρίας"),
        (LABORATORY_COURSE, "Εργαστηριακό Μάθημα"),
        (ASSIGNMENT_CORRECTION, "Διόρθωση Εργασίας"),
        (TUTORIAL_COURSE, "Φροντιστηριακό Μάθημα"),
    ]

    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    
    year = models.IntegerField(null=True)
    teaching_type = models.CharField(null=True, choices=TEACHING_TYPES)
    hours_per_week = models.IntegerField(null=True)	
    no_weeks = models.IntegerField(null=True)	
    have_contract = models.BooleanField(null=True)
    comments = models.TextField(null=True)

    approved_by_faculty = models.BooleanField(null=True, default=None)
    approved_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.course.title_gr + ' [' + self.course.code_gr + '] : ' + self.teaching_type

    def save(self, *args, **kwargs):
        if self.candidate and self.candidate.supervisor:
            self.faculty = self.candidate.supervisor
        
        if self.approved_by_faculty == True:
            self.approved_date = date.today()
        
        new = self.id is None
        super().save(*args, **kwargs)

        if new:
            self.notify_creation()
        elif self.approved_by_faculty == True:
            self.notify_approve()
        else:
            self.notify_reject()

    def notification_dict(self):
        return {
            'candidate' : self.candidate.display_name,
            'course' : self.course,
            'teaching_type' : self.teaching_type
        }
    
    def creation_notification(self):
        template = Template(TEACHING_CREATION_NOTIFICATION)
        return template.render({ 'p' : self.notification_dict() })
    
    def approved_notification(self):
        template = Template(TEACHING_APPROVED_NOTIFICATION)
        return template.render({ 'p' : self.notification_dict() })
    
    def rejected_notification(self):
        template = Template(TEACHING_REJECTED_NOTIFICATION)
        return template.render({ 'p' : self.notification_dict() })
    
    
    def notify_creation(self):
        notify(self.faculty.email, 'Δημιουργία Νέου Επικουρικού Έργου', self.creation_notification()) # Cc argument may be added in production. Skipped in order not to sending mails in original mailer.

    def notify_approve(self):
        notify(self.candidate.email, 'Έγκριση Επικουρικού Έργου', self.approved_notification()) # Cc argument may be added in production. Skipped in order not to sending mails in original mailer.

    def notify_reject(self):
        notify(self.candidate.email, 'Απόρριψη Επικουρικού Έργου', self.rejected_notification()) # Cc argument may be added in production. Skipped in order not to sending mails in original mailer.


class AnnualReport(models.Model):

    SUFFICIENT = "sufficient"
    INSUFFICIENT = "insufficient"
    SATISFACTORY = "satisfactory"

    RECOMMENDATIONS = [
        (SUFFICIENT, "Επαρκής"),
        (INSUFFICIENT, "Ανεπαρκής"),
        (SATISFACTORY, "Ικανοποιητική"),
    ]

    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(StaffMember, null=True, blank=True,  on_delete=models.SET_NULL)

    report = models.FileField(null=True) 
    year = models.IntegerField(null=True)
    comments = models.TextField(null=True)

    recommendation = models.CharField(null=True, choices=RECOMMENDATIONS, default=None)
    recommendation_datetime = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.candidate and self.candidate.supervisor:
            self.faculty = self.candidate.supervisor
        
        if self.recommendation == None:
            self.recommendation_datetime = datetime.now()