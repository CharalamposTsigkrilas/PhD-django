from django.db import models
from django.contrib.auth.models import User
from myprofile.models import StaffMember, create_user_if_required

# Create your models here.

class PhDStudent(models.Model):

    username = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    display_name = models.CharField(max_length=200, null=True, blank=True)

    id_number = models.CharField(max_length=70, null=True)
    email = models.EmailField(null=True)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    fathers_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    external_email = models.EmailField(null=True)
    gender = models.CharField()
    mobile_phone = models.CharField(max_length=30,blank=True, null=True)
    home_phone = models.CharField(max_length=30,blank=True, null=True)
    home_address = models.CharField(max_length=70, null=True, blank=True)
    subject_gr = models.CharField()
    subject_en = models.CharField()
    inscription_date = models.DateField()
    inscription_ref = models.CharField()
    photo = models.ImageField(null=True, blank=True)
    cv_gr = models.TextField()
    cv_en = models.TextField()
    scopus_id = models.CharField()

    supervisor = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL)
    member1 = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL)
    member2 = models.ForeignKey(StaffMember, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.display_name = self.given_name + ' ' + self.surname
        if not self.id:
            user = create_user_if_required(self.email)
            if user:
                self.user = user
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name   