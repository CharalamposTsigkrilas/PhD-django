from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import StaffMember, Associate, Student, PhdStudent
from .checks import is_staff_member, is_associate, is_secreteriat, is_internal_staff_member, is_student, is_phd_student
from .forms import StaffFormRestricted, AssociateFormRestricted, AssociateForm, StaffForm, StudentFormRestricted, PhdStudentForm, PhdStudentFormRestricted, PhdStudentFormRestrictedForStaff
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from dal import autocomplete
from sis import sis
from theses.models import Thesis

# Create your views here.


def render_anauthorized_staff(request):
     return render(request, 'myprofile/message.html',
                       context = {'message' : 
                                  """
                                  Δεν είστε δηλωμένος στο σύστημα ως μέλος του ιδρύματος. </br>
                                  Σε περίπτωση που χρειάζεται να χρησιμοποιήσετε την εφαρμογή επικοινωνήστε 
                                  με τον διαχειριστή <a href="mailto:thkam@hua.gr"> εδώ </a>
                                  """})

@login_required
def staff_profile(request):
    profile = StaffMember.objects.get(user = request.user)
    if request.method == 'POST':
        form = StaffFormRestricted(request.POST, instance = profile)

        if form.is_valid():
            form.save()
            return reverse_lazy('myprofile:index')
        else:
            return render(request, 'myprofile/profile.html', context = {'form' : form})
    else:
        form = StaffFormRestricted(instance=profile)
        return render(request, 'myprofile/profile.html', context={'form' : form})

@login_required
def associate_profile(request):
    profile = Associate.objects.get(user = request.user)
    if request.method == 'POST':
        form = AssociateFormRestricted(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('myprofile:index')
        else:
            return render(request, 'myprofile/profile.html', context = {'form' : form})
    else:
        form = AssociateFormRestricted(instance = profile)
        return render(request, 'myprofile/profile.html', context={'form' : form})

@login_required
def student_profile(request):
    profile = get_object_or_404(Student, user = request.user)
    form = StudentFormRestricted(instance = profile)
    thesis = Thesis.objects.filter(assigned_to = profile)
    if thesis.count() == 1:
        thesis = thesis[0]
    else:
        thesis = None
    
    return render(request, 'myprofile/studentprofile.html', context={'form' : form, 'thesis' : thesis})

class PhdStudentProfileView(LoginRequiredMixin, generic.UpdateView):
    model = PhdStudent
    template_name = "myprofile/phdstudentprofile.html"
    form_class = PhdStudentFormRestricted
    success_url = reverse_lazy('myprofile:index')

    def get_object(self, queryset=None):
        return get_object_or_404(PhdStudent, user=self.request.user)

@login_required
def index(request):
    
    if is_secreteriat(request.user):
        return redirect('myprofile:list_associates')
    elif is_staff_member(request.user) :
        return staff_profile(request)        
    elif is_associate(request.user):
        return associate_profile(request)
    elif is_student(request.user):
        return student_profile(request)
    elif is_phd_student(request.user):
        # return phd_student_profile(request)
        return PhdStudentProfileView.as_view()(request)
    
    else:
        return render_anauthorized_staff(request)

@login_required
def logout_view(request):
    logout(request)
    return render(request, 
                  'myprofile/message.html', 
                  context = {'message' : 
                             """
                             Αποσυνδεθήκατε από το σύστημα. </br>
                             Ευχαριστούμε που χρησιμοποιήσατε την υπηρεσία μας. </br>
                             Συνδεθείτε ξανά <a href="https://mydep.ditapps.hua.gr"> εδώ </a>
                             """})
                             
class list_associates(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "myprofile/list_associates.html"
    context_object_name = "associates"

    def test_func(self):
        return is_secreteriat(self.request.user)

    def get_queryset(self):
        return Associate.objects.all()
    
class edit_associate(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Associate
    template_name = "myprofile/profile.html"
    form_class = AssociateForm
    success_url = reverse_lazy('myprofile:list_associates')

    def test_func(self):
        return is_secreteriat(self.request.user)

class create_associate(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = Associate
    template_name = "myprofile/profile.html"
    form_class = AssociateForm
    success_url = reverse_lazy('myprofile:list_associates')

    def test_func(self):
        return is_secreteriat(self.request.user)

@login_required
@user_passes_test(is_secreteriat)    
def delete_associate(request, pk):
    obj = get_object_or_404(Associate, pk=pk)
    obj.delete()
    return redirect('myprofile:list_associates')

class staff_list_associates(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "myprofile/staff_list_associates.html"
    context_object_name = "associates"

    def test_func(self):
        return is_internal_staff_member(self.request.user)

    def get_queryset(self):
        p = StaffMember.objects.get(user = self.request.user)
        return Associate.objects.filter(supervisor = p)

class staff_edit_associate(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Associate
    template_name = "myprofile/profile.html"
    form_class = AssociateFormRestricted
    success_url = reverse_lazy('myprofile:staff_list_associates')

    def test_func(self):      
        return is_internal_staff_member(self.request.user) 

    def get_queryset(self):
        q = super().get_queryset()
        p = StaffMember.objects.get(user = self.request.user)        
        return q.filter(supervisor = p)
    
@login_required
@user_passes_test(is_secreteriat)    
def delete_associate(request, pk):
    obj = get_object_or_404(Associate, pk=pk)
    obj.delete()
    return redirect('myprofile:list_associates')
    
@login_required
@user_passes_test(is_secreteriat)    
def staff_delete_associate(request, pk):
    p = StaffMember.objects.get(user = request.user)
    obj = get_object_or_404(Associate, pk=pk, supervisor=p)
    obj.delete()
    return redirect('myprofile:staff_list_associates')

"""
Faculty CRUD views
"""

class list_staff(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "myprofile/list_staff.html"
    context_object_name = "staff"

    def test_func(self):
        return is_secreteriat(self.request.user)

    def get_queryset(self):
        return StaffMember.objects.all()
    
class edit_staff(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = StaffMember
    template_name = "myprofile/staff_edit.html"
    form_class = StaffForm
    success_url = reverse_lazy('myprofile:list_staff')

    def test_func(self):
        return is_secreteriat(self.request.user)

class create_staff(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = StaffMember
    template_name = "myprofile/staff_edit.html"
    form_class = StaffForm
    success_url = reverse_lazy('myprofile:list_staff')

    def test_func(self):
        return is_secreteriat(self.request.user)

@login_required
@user_passes_test(is_secreteriat)    
def delete_staff(request, pk):
    obj = get_object_or_404(StaffMember, pk=pk)
    obj.delete()
    return redirect('myprofile:list_staff')

class StaffMemberAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = StaffMember.objects.all()
        if self.q:
            qs = qs.filter(display_name__contains=self.q)
        
        return qs

class StudentAutocomplete(UserPassesTestMixin, LoginRequiredMixin, autocomplete.Select2ListView):
    
    def test_func(self):
        return is_secreteriat(self.request.user) or is_staff_member(self.request.user)
    
    def get_list(self):
        entries = sis.estudiesdb().filter_students(self.q)
        print(entries)
        if not entries:
            return []
        else:
            return [ [ e['UserName'], e['SurName'] + ' ' + e['FirstName'] + ' (' + e['UserName'] + ')' ] for e in entries ]
            #return [ [ e['UserName'], e['UserName'] ] for e in entries ]




# CRUD (Create, Read, Update, Delete) views for PhD Students


# Secreatary can CRUD everything

class sec_list_phd_students(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "myprofile/sec_list_phd_students.html"
    context_object_name = "phdstudents"

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_queryset(self):
        return PhdStudent.objects.all()
    
class sec_edit_phd_student(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = PhdStudent
    template_name = "myprofile/sec_edit_phd_student.html"
    form_class = PhdStudentForm
    success_url = reverse_lazy('myprofile:sec_list_phd_students')
    
    def test_func(self):
        return is_secreteriat(self.request.user)

class sec_create_phd_student(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = PhdStudent
    template_name = "myprofile/sec_edit_phd_student.html"
    form_class = PhdStudentForm
    success_url = reverse_lazy('myprofile:sec_list_phd_students')
    
    def test_func(self):
        return is_secreteriat(self.request.user)


@login_required
@user_passes_test(is_secreteriat)    
def sec_delete_phd_student(request, pk):
    obj = get_object_or_404(PhdStudent, pk=pk)
    obj.delete()
    return redirect('myprofile:sec_list_phd_students')


# Staff Members of a PhD student can only see (Read) the PhD's student data

class staff_list_phd_students(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "myprofile/staff_list_phd_students.html"
    context_object_name = "phdstudents"

    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_queryset(self):
        staff_member = StaffMember.objects.get(user=self.request.user)
        return PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))


class staff_spectate_phd_student(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = PhdStudent
    template_name = "myprofile/staff_spectate_phd_student.html"
    context_object_name = "phdstudent"
    
    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhdStudentFormRestrictedForStaff(instance=self.object) 
        return context