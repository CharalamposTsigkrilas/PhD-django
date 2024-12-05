from .models import StaffMember, Associate, Student

def is_staff_member(user):
    s = StaffMember.objects.filter(user = user)
    return s.count() == 1

def is_internal_staff_member(user):
    s = StaffMember.objects.filter(user = user, is_internal = True)
    return s.count() == 1

def is_associate(user):
    s = Associate.objects.filter(user = user)
    return s.count() == 1

def is_secreteriat(user):
    return user.has_perm('myprofile.is_secreteriat')

def likely_student_username(user):
    return user.username.startswith('it') or user.username.startswith('csi')

def is_student(user):
    s = Student.objects.filter(user = user)
    return s.count() == 1
