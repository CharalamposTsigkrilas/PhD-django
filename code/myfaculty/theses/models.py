from django.db import models

# Create your models here.
from django.db import models
from myprofile.models import StaffMember, Student
from curricula.models import StudyProgram
from datetime import datetime
from jinja2 import Template
from django.conf import settings

class Thesis(models.Model):

    supervisor = models.ForeignKey(StaffMember, null=True, on_delete=models.SET_NULL )
    member1 = models.ForeignKey(StaffMember, null=True, on_delete=models.SET_NULL, related_name='thesis_member1' )
    member2 = models.ForeignKey(StaffMember, null=True, on_delete=models.SET_NULL, related_name='thesis_member2' )
    title_gr = models.CharField(max_length=300, null=True)
    title_en = models.CharField(max_length=300, null=True)
    abstract = models.TextField(null=True)
    offered_in = models.ManyToManyField(StudyProgram)    
    updated_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    is_offered = models.BooleanField(null=True, default=True)
    assigned_to = models.ForeignKey(Student, on_delete = models.SET_NULL, null=True, blank=True)
    assigned_to_char = models.CharField(max_length = 300, null=True, blank=True, help_text='Πληκτρολογείστε τουλάχιστον τρεις χαρακτήρες')
    assignment_ga = models.CharField(max_length=300, null=True, blank=True)
    assignment_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    grade_sup = models.IntegerField(null=True, blank=True)
    grade_member1 = models.IntegerField(null=True, blank=True)
    grade_member2 = models.IntegerField(null=True, blank=True)
    grade_avg = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title_gr + ' ('+ self.supervisor.display_name + ') '
    
    def save(self, *args, **kwargs):
        new = self.id is  None
        
        if not self.id and not self.created_date:
            self.created_date = datetime.now()

        if self.id and not self.updated_date:
            self.updated_date = datetime.now()

        if self.grade_member1 and self.grade_member2 and self.grade_sup:
            self.grade_avg = round( 1/3 * (self.grade_member1 + self.grade_member2 + self.grade_sup) )
        super().save(*args, **kwargs)

        