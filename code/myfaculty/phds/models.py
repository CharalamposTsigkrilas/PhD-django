from django.db import models
from myprofile.models import StaffMember, PhdStudent
from curricula.models import Course
from datetime import date

# Create your models here.

class JournalPublication(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField()
    authors_list = models.TextField()
    has_supervisor = models.BooleanField()
    journal = models.CharField()
    publisher = models.CharField()
    volume = models.CharField()
    issue = models.CharField()
    year = models.IntegerField()
    doi = models.CharField()

class ConferencePublication(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField()
    authors_list = models.TextField()	
    conference_name = models.CharField()	
    venue = models.CharField()
    year = models.IntegerField()
    has_supervisor = models.BooleanField()

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
    
    year = models.IntegerField()
    teaching_type = models.CharField(max_length=50, choices=TEACHING_TYPES)
    hours_per_week = models.IntegerField()	
    no_weeks = models.IntegerField()	
    have_contract = models.BooleanField()
    comments = models.TextField()

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
