from django.db import models
from myprofile.models import StaffMember, PhdStudent
from curricula.models import Course
from datetime import date

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

class ConferencePublication(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField(null=True)
    authors_list = models.TextField(null=True)	
    conference_name = models.CharField(null=True)	
    venue = models.CharField(null=True)
    year = models.IntegerField(null=True)
    has_supervisor = models.BooleanField(null=True)

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
    faculty = models.ForeignKey(StaffMember, null=True, blank=True,  on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    
    year = models.IntegerField(null=True)
    teaching_type = models.CharField(null=True, choices=TEACHING_TYPES)
    hours_per_week = models.IntegerField(null=True)	
    no_weeks = models.IntegerField(null=True)	
    have_contract = models.BooleanField(null=True)
    comments = models.TextField(null=True)

    approved_by_faculty = models.BooleanField(null=True, default=False)
    approved_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.candidate and self.candidate.supervisor:
            self.faculty = self.candidate.supervisor
        
        if self.approved_by_faculty == True:
            self.approved_date = date.today()
        else:
            self.approved_date = None
        
        super().save(*args, **kwargs)
