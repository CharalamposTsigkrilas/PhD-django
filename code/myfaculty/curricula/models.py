from django.db import models
from myprofile.models import StaffMember

# Create your models here.

class School(models.Model):

    title_gr = models.CharField(max_length=100)
    short_gr = models.CharField(max_length=20, null=True, blank=True)
    code_gr = models.CharField(max_length=20, null=True, blank=True)
    title_en = models.CharField(max_length=100)
    short_en = models.CharField(max_length=20, null=True, blank=True)
    code_en = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title_gr
    
class Department(models.Model):
    title_gr = models.CharField(max_length=100)
    short_gr = models.CharField(max_length=20, null=True, blank=True)
    code_gr = models.CharField(max_length=20, null=True, blank=True)
    title_en = models.CharField(max_length=100)
    short_en = models.CharField(max_length=20, null=True, blank=True)
    code_en = models.CharField(max_length=20, null=True, blank=True)    
    school = models.ForeignKey('School', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title_gr
    
class StudyProgram(models.Model):
    UNDERGRADUATE = "Προπτυχιακό"
    POSTGRADUATE = "Μεταπτυχιακό"
    DOCTORAL = "Διδακτορικό"
    POSTDOC = "Μεταδιδακτορικό"
    OTHER = "´Άλλο"

    STUDY_CHOICES = {
        UNDERGRADUATE : "Προπτυχιακό",
        POSTGRADUATE : "Μεταπτυχιακό",
        DOCTORAL : "Διδακτορικό",
        POSTDOC : "Μεταδιδακτορικό",
        OTHER : "´Άλλο"
    }

    STUDY_CHOICES_EN = {
        UNDERGRADUATE : "Undergraduate",
        POSTGRADUATE : "Postgraduate",
        DOCTORAL : "Doctoral",
        POSTDOC : "Postdoctoral",
        OTHER : "Other"
    }

    title_gr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100, null=True)
    
    short_gr = models.CharField(max_length=20, null=True, blank=True)
    short_en = models.CharField(max_length=20, null=True, blank=True)
    
    code_gr = models.CharField(max_length=20, null=True, blank=True)
    code_en = models.CharField(max_length=20, null=True, blank=True)
    
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100, choices = STUDY_CHOICES)

    sis_code = models.IntegerField(null=True)
    
    def level_gr(self):
        return self.type
    
    def level_en(self):
        return self.STUDY_CHOICES_EN[self.level_gr()]
        
    def __str__(self):
        return self.title_gr
    
    def get_courses(self):
        return Course.objects.filter(program = self)
    
class Course(models.Model):
    program = models.ForeignKey('StudyProgram', null=True, on_delete=models.SET_NULL)
    code_gr = models.CharField(max_length=20)
    code_en = models.CharField(max_length=20)    
    semester = models.FloatField()
    title_gr = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True)    
    weekly_hours = models.FloatField(null=True, blank=True)
    weekly_lab_hours = models.FloatField(null=True, blank=True)
    ects_credits = models.FloatField(null=True)
    type_gr = models.CharField(max_length=100, blank=True)
    type_en = models.CharField(max_length=100, blank=True)
    prequesites_gr = models.TextField(null=True, blank=True)
    prequesites_en = models.TextField(null=True, blank=True)    
    url = models.URLField(max_length=300, blank=True, null=True)
    language_gr = models.CharField(max_length=100, blank=True)
    language_en = models.CharField(max_length=100, blank=True)    
    offered_erasmus = models.BooleanField(default=False, null=True, blank=True)
    outcomes_gr = models.TextField(null=True, blank=True)
    outcomes_en = models.TextField(null=True, blank=True)
    skills_gr = models.TextField(null=True, blank=True)
    skills_en = models.TextField(null=True, blank=True)
    content_gr = models.TextField(null=True, blank=True)
    content_en = models.TextField(null=True, blank=True)
    delivery_gr = models.CharField(max_length=200, blank=True)
    delivery_en = models.CharField(max_length=200, blank=True)
    evaluation_gr = models.TextField(null=True, blank=True)
    evaluation_en = models.TextField(null=True, blank=True)
    ict_gr = models.TextField(null=True, blank=True)
    ict_en = models.TextField(null=True, blank=True)
    bibliography_gr = models.TextField(null=True, blank=True)
    bibliography_en = models.TextField(null=True, blank=True)
    journals = models.TextField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    required_math = models.TextField(null=True, blank=True)
    required_lab = models.TextField(null=True, blank=True)
    display_name = models.CharField(null=True, blank=True)
    assigned_to = models.ManyToManyField(StaffMember)
    elective = models.BooleanField(null=True)

    hours_lecturing = models.FloatField(null=True, blank=True)
    hours_lab = models.FloatField(null=True, blank=True)
    hours_study = models.FloatField(null=True)
    hours_project = models.FloatField(null=True)
    hours_lab_prep = models.FloatField(null=True)
    hours_total = models.FloatField(null=True)
    
    def __str__(self):
        return self.title_gr + ' [' + self.code_gr + ']'
    
    def offered_erasmus_gr(self):
        return 'Ναι' if self.offered_erasmus else 'Όχι'
    
    def offered_erasmus_en(self):
        return 'Yes' if self.offered_erasmus else 'No'
    
    def course_type_gr(self):
        if self.elective:
            part1 = 'Επιλογής'
        else:
            part1 = 'Υποχρεωτικό'

        return part1 + ' - ' + self.program.level_gr()
    
    def course_type_en(self):
        if self.elective:
            part1 = 'Elective'
        else:
            part1 = 'Compulsory'
        return part1  + ' - ' + self.program.level_en()
    
    def ects_gr_dict(self):
        return {
            'school' : self.program.department.school.title_gr,
            'department' : self.program.department.title_gr,
            'level' : self.program.level_gr(),
            'code' : self.code_gr,
            'semester' : int(self.semester),
            'offered_erasmus' : self.offered_erasmus_gr(),
            'title' : self.title_gr,
            'hours' : self.weekly_hours,
            'type' : self.course_type_gr(),
            'prequisites' : self.prequesites_gr,
            'language' : self.language_gr,
            'url' : self.url,
            'results' : self.outcomes_gr,
            'skills' : self.skills_gr,
            'content' : self.content_gr,
            'delivery' : self.delivery_gr,
            'usedict' : self.ict_gr,
            'hours_lecture' : self.hours_lecturing,
            'hours_lab' : self.hours_lab,
            'hours_project' : self.hours_project,
            'hours_study' : self.hours_study,
            'sum_hours' : self.hours_total,
            'evaluation' : self.evaluation_gr,
            'bibliography' : self.bibliography_gr,
            'journals' : self.journals            
        }

    def ects_en_dict(self):
        return {
            'school' : self.program.department.school.title_en,
            'department' : self.program.department.title_en,
            'level' : self.program.level_en(),
            'code' : self.code_en,
            'semester' : int(self.semester),
            'offered_erasmus' : self.offered_erasmus_en(),
            'title' : self.title_en,
            'hours' : self.weekly_hours,
            'type' : self.course_type_en(),
            'prequisites' : self.prequesites_en,
            'language' : self.language_en,
            'url' : self.url,
            'results' : self.outcomes_en,
            'skills' : self.skills_en,
            'content' : self.content_en,
            'delivery' : self.delivery_en,
            'usedict' : self.ict_en,
            'hours_lecture' : self.hours_lecturing,
            'hours_lab' : self.hours_lab,
            'hours_project' : self.hours_project,
            'hours_study' : self.hours_study,
            'sum_hours' : self.hours_total,
            'evaluation' : self.evaluation_en,
            'bibliography' : self.bibliography_en,
            'journals' : self.journals            
        }

    def to_dict(self):
        obj = self
        return {
            "id": obj.id,
            "program": obj.program.title_gr,
            "code_gr": obj.code_gr,
            "code_en": obj.code_en,
            "semester": obj.semester,
            "title_gr": obj.title_gr,
            "title_en": obj.title_en,
            "weekly_hours": obj.weekly_hours,
            "weekly_lab_hours": obj.weekly_lab_hours,
            "ects_credits": obj.ects_credits,
            "type_gr": obj.type_gr,
            "type_en": obj.type_en,
            "prequesites_gr": obj.prequesites_gr,
            "prequesites_en": obj.prequesites_en,
            "url": obj.url,
            "language_gr": obj.language_gr,
            "language_en": obj.language_en,
            "offered_erasmus": obj.offered_erasmus,
            "outcomes_gr": obj.outcomes_gr,
            "outcomes_en": obj.outcomes_en,
            "skills_gr": obj.skills_gr,
            "skills_en": obj.skills_en,
            "content_gr": obj.content_gr,
            "content_en": obj.content_en,
            "delivery_gr": obj.delivery_gr,
            "delivery_en": obj.delivery_en,
            "evaluation_gr": obj.evaluation_gr,
            "evaluation_en": obj.evaluation_en,
            "ict_gr": obj.ict_gr,
            "ict_en": obj.ict_en,
            "bibliography_gr": obj.bibliography_gr,
            "bibliography_en": obj.bibliography_en,
            "journals": obj.journals,
            "active": obj.active,
            "required_math": obj.required_math,
            "required_lab": obj.required_lab,
            "display_name": obj.display_name,
            "elective": obj.elective,
            "hours_lecturing": obj.hours_lecturing,
            "hours_lab": obj.hours_lab,
            "hours_study": obj.hours_study,
            "hours_project": obj.hours_project,
            "hours_lab_prep": obj.hours_lab_prep,
            "hours_total": obj.hours_total,
        }

class Director(models.Model):

    programs = models.ManyToManyField('StudyProgram')
    staffmember = models.ForeignKey(StaffMember,null=True, on_delete=models.SET_NULL)



    
    




    
    