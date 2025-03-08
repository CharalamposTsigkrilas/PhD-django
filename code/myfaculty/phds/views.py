from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import JournalPublication, ConferencePublication, Teaching
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from myprofile.checks import is_phd_student, is_secreteriat, is_staff_member
from myprofile.models import StaffMember, PhdStudent
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy

# Create your views here.


# phds views --> PhD students create and spectate only
        
    # Journals

class phd_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    template_name = "phds/phd_list_journals.html"
    context_object_name = "journals"

    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_queryset(self):
        p = PhdStudent.objects.get(user = self.request.user)
        return JournalPublication.objects.filter(candidate = p)

class phd_create_journal(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = JournalPublication
    # template_name = "phds/phd_journal_edit.html"
    # form_class = JournalForm
    # success_url = reverse_lazy('phds:phd_list_journals')

    # def test_func(self):
    #     return is_phd_student(self.request.user)    
    def dummy():
        return
    
class phd_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return
    
    
    # Conferences

class phd_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/phd_list_conferences.html"
    context_object_name = "conferences"

    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_queryset(self):
        p = PhdStudent.objects.get(user = self.request.user)
        return ConferencePublication.objects.filter(candidate = p)

class phd_create_conference(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = ConferencePublication
    # template_name = "phds/phd_conference_edit.html"
    # form_class = ConferenceForm
    # success_url = reverse_lazy('phds:phd_list_conferences')

    # def test_func(self):
    #     return is_phd_student(self.request.user)
    def dummy():
        return
    
class phd_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return  
    
    
    # Teachings

class phd_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/phd_list_teachings.html"
    context_object_name = "teachings"

    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_queryset(self):
        p = PhdStudent.objects.get(user = self.request.user)
        return Teaching.objects.filter(candidate = p)

class phd_create_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = Teaching
    # template_name = "phds/phd_teaching_edit.html"
    # form_class = TeachingForm
    # success_url = reverse_lazy('phds:phd_list_teachings')

    # def test_func(self):
    #     return is_phd_student(self.request.user)
    def dummy():
        return
    
class phd_spectate_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return




# staff views --> Staff Members spectate only and accepting/rejecting Teaching --> Only for the PhDs they have.
    
    # Journals

class staff_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    template_name = "phds/staff_list_journals.html"
    context_object_name = "journals"

    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_queryset(self):
        staff_member = StaffMember.objects.get(user=self.request.user)
        staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
        return JournalPublication.objects.filter(candidate__in=staff_member_phd_list)

# @login_required
# @user_passes_test(is_staff_member)
# def staff_list_journals(request, pk):
#     p = get_object_or_404(PhdStudent, pk=pk)
#     journals = JournalPublication.objects.filter(candidate=p)
#     return render(request, "phds/staff_list_journals.html", {"journals": journals})

class staff_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return
    
    
    # Conferences

class staff_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/staff_list_conferences.html"
    context_object_name = "conferences"

    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_queryset(self):
        staff_member = StaffMember.objects.get(user=self.request.user)
        staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
        return ConferencePublication.objects.filter(candidate__in=staff_member_phd_list)

class staff_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return    
    
    
    # Teaching

class staff_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/staff_list_teachings.html"
    context_object_name = "teachings"

    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_queryset(self):
        staff_member = StaffMember.objects.get(user=self.request.user)
        staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
        return Teaching.objects.filter(candidate__in=staff_member_phd_list)

class staff_spectate_accept_reject_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return
    


# sec views --> Secreatary CRUD everything
    
    # Journals

class sec_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    template_name = "phds/sec_list_journals.html"
    context_object_name = "journals"

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_queryset(self):
        return JournalPublication.objects.all()

class sec_create_journal(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = JournalPublication
    # template_name = "phds/sec_journal_edit.html"
    # form_class = JournalForm
    # success_url = reverse_lazy('phds:sec_list_journals')

    # def test_func(self):
    #     return is_secreteriat(self.request.user)
    def dummy():
        return

class sec_update_journal(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_journal():
    return
    
    
    # Conferences

class sec_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/sec_list_conferences.html"
    context_object_name = "conferences"

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_queryset(self):
        return ConferencePublication.objects.all()
    
class sec_create_conference(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = ConferencePublication
    # template_name = "phds/sec_conference_edit.html"
    # form_class = ConferenceForm
    # success_url = reverse_lazy('phds:sec_list_conferences')

    # def test_func(self):
    #     return is_secreteriat(self.request.user)
    def dummy():
        return

class sec_update_conference(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_conference():
    return


    # Teaching

class sec_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    template_name = "phds/sec_list_teachings.html"
    context_object_name = "teachings"

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_queryset(self):
        return Teaching.objects.all()

class sec_create_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    # model = Teaching
    # template_name = "phds/sec_teaching_edit.html"
    # form_class = TeachingForm
    # success_url = reverse_lazy('phds:sec_list_teachings')

    # def test_func(self):
    #     return is_secreteriat(self.request.user)
    def dummy():
        return

class sec_update_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_teaching():
    return