from django import template
from myprofile.models import StaffMember, Student, PhdStudent

register = template.Library()

@register.filter(name="is_staff_member")
def is_staff_member(user):
    p = StaffMember.objects.filter(user= user)
    return p.count() > 0

@register.filter(name="is_student")
def is_student(user):
    p = Student.objects.filter(user= user)
    return p.count() > 0

@register.filter(name="is_phd_student")
def is_phd_student(user):
    p = PhdStudent.objects.filter(user= user)
    return p.count() > 0