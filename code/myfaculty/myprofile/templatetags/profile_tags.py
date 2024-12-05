from django import template
from myprofile.models import StaffMember, Student

register = template.Library()

@register.filter(name="is_staff_member")
def is_staff_member(user):
    p = StaffMember.objects.filter(user= user)
    return p.count() > 0

@register.filter(name="is_student")
def is_staff_member(user):
    p = Student.objects.filter(user= user)
    return p.count() > 0