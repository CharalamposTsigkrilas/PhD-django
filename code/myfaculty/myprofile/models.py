from django.db import models
from django.contrib.auth.models import User
from sis import sis
# Create your models here.

def create_user_if_required(email):
    username = email.split('@')[0]
    no_users = User.objects.filter(username=username).count()
    if no_users == 0:
        user = User(username=username, email=email)
        user.save()
        return user
    else:
        return None
    
class StaffMember(models.Model):
    """
    The basic staff member class. Stores information related to faculty members
    """
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    email = models.EmailField(null=True)    
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    fathers_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    display_name_full = models.CharField(max_length=200, null=True, blank=True)
    
    tin = models.CharField(max_length=50, null=True, blank=True)
    ssn = models.CharField(max_length=50, null=True,blank=True)

    is_internal = models.BooleanField(null=True, default=True)
    
    institution = models.CharField(max_length=100, default='Χαροκόπειο Πανεπιστήμιο')
    school = models.CharField(max_length=100, default = 'Ψηφιακής Τεχνολογίας')        
    department = models.CharField(max_length=100, default = 'Πληροφορικής και Τηλεματικής')        
    
    title = models.CharField(max_length=70, null=True)
    
    home_address_street = models.CharField(max_length=70, null=True, blank=True)
    home_address_no = models.IntegerField(null=True, blank=True)
    home_address_po_box = models.CharField(max_length=30, null=True, blank=True)
    home_address_city = models.CharField(max_length=70, null=True, blank=True)
    home_address_country = models.CharField(max_length=70, null=True, default = 'Ελλάδα', blank=True)
    mobile_phone = models.CharField(max_length=30,blank=True, null=True)    
    home_phone = models.CharField(max_length=30,blank=True, null=True)

    work_address_street = models.CharField(max_length=70, null=True, default = 'Ομήρου')
    work_address_no = models.CharField(max_length=10,null=True, default='9')    
    work_address_po_box = models.CharField(max_length=30, null=True, default = '17778')
    work_address_city = models.CharField(max_length=70, null=True, default = 'Αθήνα')
    work_address_country = models.CharField(max_length=70, null=True, default = 'Ελλάδα')
    work_phone = models.CharField(max_length=20,blank=True, null=True)

    pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.display_name_full
    
    def save(self, *args, **kwargs):
        self.display_name = self.given_name + ' ' + self.surname
        self.display_name_full = self.display_name + ' (' + self.title + ')'
        if not self.id:
            user = create_user_if_required(self.email)
            if user:
                self.user=user
        
        super().save(*args, **kwargs)

class Associate(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    email = models.EmailField(null=True)    
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    fathers_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    display_name_full = models.CharField(max_length=200, null=True, blank=True)

    tin = models.CharField(max_length=50, null=True, blank=True)
    ssn = models.CharField(max_length=50, null=True, blank=True)

    is_phd_student = models.BooleanField(null=True, default=False)
    is_postdoc = models.BooleanField(null=True, default=False)
    
    home_address_street = models.CharField(max_length=70, null=True, blank=True)
    home_address_no = models.IntegerField(null=True, blank=True)
    home_address_po_box = models.CharField(max_length=30, null=True, blank=True)
    home_address_city = models.CharField(max_length=70, null=True, default = 'Αθήνα', blank=True)
    home_address_country = models.CharField(max_length=70, null=True, default = 'Ελλάδα', blank=True)
    mobile_phone = models.CharField(max_length=30,blank=True, null=True)    
    home_phone = models.CharField(max_length=30,blank=True, null=True) 
    work_phone = models.CharField(max_length=30,blank=True, null=True) 

    card_no = models.CharField(max_length=40,blank=True, null=True)
    seat_no = models.CharField(max_length=40,blank=True, null=True)
    office_no = models.CharField(max_length=40,blank=True, null=True)

    supervisor = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL)
    
    def save(self, *args, **kwargs):
        self.display_name = self.given_name + ' ' + self.surname
        if not self.id:
            user = create_user_if_required(self.email)
            if user:
                self.user=user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name
    
class CustomUserPermissions(models.Model):
    class Meta:
        permissions = (
            ("is_secreteriat", "Is a secreteriat user"),
        )

class StudentManager(models.Manager):

    def get_profile(self, username):      
        P = Student.objects.filter(user__username = username)
        
        # No such student profile exists
        if len(P) == 0:
            P_new = Student(username = username)
            P_new.save()
            return P_new
        else:
            return P[0]


class Student(models.Model):

    username = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)    
    email = models.EmailField(null=True)    
    given_name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=70, null=True)
    semester = models.IntegerField(null=True)
    program = models.ForeignKey('curricula.StudyProgram', null=True, on_delete=models.SET_NULL)
    reg_num = models.CharField(max_length=70, null=True)
    display_name = models.CharField(max_length=200, null=True)

    objects = StudentManager()
    
    def save(self, *args, **kwargs):

        from curricula.models import StudyProgram

        username = self.username
        e = sis.estudiesdb().get_student_data(username)
        print(e['DeptPrg'])
        self.email = username + '@hua.gr'
        self.given_name = e['FirstName']
        self.surname = e['SurName']
        self.semester = e['TrexonEksamFoit']
        self.reg_num = e['Mhtrwo']
        
        user = User.objects.filter(username = self.username)
        if user.count() == 0:
            self.user = User(username = username, email = self.email)
            self.user.save()
        else:
            self.user = user[0]

        program = StudyProgram.objects.filter(sis_code = e['DeptPrg'])
        if program.count() == 1:
            self.program = program[0]

        self.display_name = self.given_name + ' ' + self.surname

        super().save(*args, **kwargs)

    def __str__(self):
        if self.display_name:
            return self.display_name
        else:
            return str(self.id)
    
class PhdStudent(models.Model):

    username = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    display_name = models.CharField(max_length=200, null=True, blank=True)

    reg_num = models.CharField(max_length=70, null=True)
    email = models.EmailField(null=True)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    fathers_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    external_email = models.EmailField(null=True)
    gender = models.CharField()
    mobile_phone = models.CharField(max_length=30,blank=True, null=True)
    home_phone = models.CharField(max_length=30,blank=True, null=True)
    home_address_street = models.CharField(max_length=70, null=True, blank=True)
    subject_gr = models.CharField()
    subject_en = models.CharField()
    inscription_date = models.DateField()
    inscription_ref = models.CharField()
    photo = models.ImageField(null=True, blank=True)
    cv_gr = models.TextField()
    cv_en = models.TextField()
    scopus_id = models.CharField()

    supervisor = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL, related_name="supervised_students")
    member1 = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL, related_name="committee_member1_students")
    member2 = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL, related_name="committee_member2_students")

    def save(self, *args, **kwargs):
        self.display_name = self.given_name + ' ' + self.surname
        if not self.id:
            user = create_user_if_required(self.email)
            if user:
                self.user = user                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name