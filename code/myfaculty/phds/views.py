from django.shortcuts import render
from .models import PhDStudent
from django.views import generic
from myprofile.checks import is_staff_member, is_secreteriat

# Create your views here.


# CRUD (Create, Read, Update, Delete) views for PhD Students App


# Secreatary can CRUD everything

# Create View - Secretary
class sec_create_phd_student():
    def dumb_return(self):
        print("sec_create_phd_student")
    
# Read View - Secretary
class sec_list_phd_students():
    def dumb_return(self):
        print("sec_list_phd_students")
    
# Upadate View - Secretary
class sec_edit_phd_student():
    def dumb_return(self):
        print("sec_edit_phd_student")
    
# Delete View - Secretary
class sec_delete_phd_student():
    def dumb_return(self):
        print("sec_delete_phd_student")


# Staff Members of a PhD student can only see (Read) the PhD's student data

# Read View - Staff Member
class staff_list_phd_students():
    def dumb_return(self):
        print("staff_list_phd_students")


# PhD student can only see (Read) their profile and add a picture (Update)

# Read View - PhD Student
class phd_student_profile():
    def dumb_return(self):
        print("phd_student_profile")

# Update View - PhD Student
class phd_student_edit():
    def dumb_return(self):
        print("phd_student_edit")