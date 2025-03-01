from django.db import models
from myprofile.models import StaffMember, PhdStudent
from curricula.models import Course
# Create your models here.

class Journal(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    title = models.TextField()
    authorsList = models.TextField()
    hasSupervisor = models.BooleanField()
    journal = models.CharField()
    publisher = models.CharField()
    volume = models.CharField()
    issue = models.CharField()
    year = models.IntegerField()
    doi = models.CharField()

class Conferense(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)

    ttitle = models.TextField()
    authorsList = models.TextField()	
    conferenceName = models.CharField()	
    venue = models.CharField()
    year = models.IntegerField()
    hasSupervisor = models.BooleanField()

class Teaching(models.Model):
    candidate = models.ForeignKey(PhdStudent, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(StaffMember, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    year = models.IntegerField()
    teachingType = {
        THEORY_LECTURE : "Διάλεξη Θεωρίας",
        LABORATORY_COURSE : "Εργαστηριακό Μάθημα",
        ASSIGNMENT_CORRECTION : "Διόρθωση Εργασίας",
        TUTORIAL_COURSE : "Φροντιστηριακό Μάθημα"
    } 
    hoursPerWeek = models.IntegerField()	
    noWeeks = models.IntegerField()	
    haveContract = models.BooleanField()
    comments = models.TextField()

    approvedByFaculty = models.BooleanField()
    approvedDate = models.DateField()
