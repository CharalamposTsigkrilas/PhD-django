from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import JournalPublication, ConferencePublication, Teaching
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from myprofile.checks import is_phd_student, is_secreteriat, is_staff_member
from myprofile.models import StaffMember, PhdStudent
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy, reverse
from .forms import *

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
    model = JournalPublication
    template_name = "phds/phd_create_journal.html"
    form_class = PhdCreateJournalForm
    success_url = reverse_lazy('phds:phd_list_journals')

    def test_func(self):
        return is_phd_student(self.request.user)    
    
    def form_valid(self, form):
        form.instance.candidate = PhdStudent.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class phd_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    model = JournalPublication
    template_name = "phds/phd_spectate_journal.html"
    context_object_name = "journal"
    
    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhdSpectateJournalFormRestricted(instance=self.object)
        return context
    
    
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
    model = ConferencePublication
    template_name = "phds/phd_create_conference.html"
    form_class = PhdCreateConferenceForm
    success_url = reverse_lazy('phds:phd_list_conferences')

    def test_func(self):
        return is_phd_student(self.request.user)

    def form_valid(self, form):
        form.instance.candidate = PhdStudent.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class phd_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    model = ConferencePublication
    template_name = "phds/phd_spectate_conference.html"
    context_object_name = "conference"
    
    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhdSpectateConferenceFormRestricted(instance=self.object)
        return context 
    
    
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
    model = Teaching
    template_name = "phds/phd_create_teaching.html"
    form_class = PhdCreateTeachingForm
    success_url = reverse_lazy('phds:phd_list_teachings')

    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["candidate"] = PhdStudent.objects.get(user=self.request.user)  # Pass PhD student
        return kwargs

    def form_valid(self, form):
        form.instance.candidate = PhdStudent.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class phd_spectate_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    model = Teaching
    template_name = "phds/phd_spectate_teaching.html"
    context_object_name = "teaching"
    
    def test_func(self):
        return is_phd_student(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PhdSpectateTeachingFormRestricted(instance=self.object)
        return context



# staff views --> Staff Members spectate only and accepting/rejecting Teaching --> Only for the PhDs they have.
    
    # Journals

# class staff_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
#     template_name = "phds/staff_list_journals.html"
#     context_object_name = "journals"

#     def test_func(self):
#         return is_staff_member(self.request.user)
    
#     def get_queryset(self):
#         staff_member = StaffMember.objects.get(user=self.request.user)
#         staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
#         return JournalPublication.objects.filter(candidate__in=staff_member_phd_list)

# @login_required
# @user_passes_test(is_staff_member)
# def staff_list_journals(request, pk):
#     p = get_object_or_404(PhdStudent, pk=pk)
#     journals = JournalPublication.objects.filter(candidate=p)
#     return render(request, "phds/staff_list_journals.html", {"journals": journals})

class staff_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    model = JournalPublication
    template_name = "phds/staff_spectate_journal.html"
    context_object_name = "journal"
    
    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StaffSpectateJournalFormRestricted(instance=self.object)
        return context
    
    
    # Conferences

# class staff_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
#     template_name = "phds/staff_list_conferences.html"
#     context_object_name = "conferences"

#     def test_func(self):
#         return is_staff_member(self.request.user)
    
#     def get_queryset(self):
#         staff_member = StaffMember.objects.get(user=self.request.user)
#         staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
#         return ConferencePublication.objects.filter(candidate__in=staff_member_phd_list)

class staff_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    model = ConferencePublication
    template_name = "phds/staff_spectate_conference.html"
    context_object_name = "conference"
    
    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StaffSpectateConferenceFormRestricted(instance=self.object)
        return context
    
    
    # Teaching

# class staff_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
#     template_name = "phds/staff_list_teachings.html"
#     context_object_name = "teachings"

#     def test_func(self):
#         return is_staff_member(self.request.user)
    
#     def get_queryset(self):
#         staff_member = StaffMember.objects.get(user=self.request.user)
#         staff_member_phd_list = PhdStudent.objects.filter(Q(supervisor=staff_member) | Q(member1=staff_member) | Q(member2=staff_member))
#         return Teaching.objects.filter(candidate__in=staff_member_phd_list)

class staff_spectate_teaching_accept_reject(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    model = Teaching
    template_name = "phds/staff_spectate_teaching_accept_reject.html"
    form_class = StaffSpectateAcceptRejectTeachingFormRestricted
    # success_url = reverse_lazy('phds:staff_list_teachings')

    def test_func(self):
        return is_staff_member(self.request.user)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:staff_spectate_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
    


# sec views --> Secreatary CRUD everything
    
    # Journals

# class sec_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
#     template_name = "phds/sec_list_journals.html"
#     context_object_name = "journals"

#     def test_func(self):
#         return is_secreteriat(self.request.user)
    
#     def get_queryset(self):
#         return JournalPublication.objects.all()

class sec_create_journal(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    model = JournalPublication
    template_name = "phds/sec_edit_journal.html"
    form_class = SecCreateJournalForm
    # success_url = reverse_lazy('phds:sec_list_journals')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        candidate_id = self.kwargs.get("pk")
        kwargs["candidate"] = get_object_or_404(PhdStudent, id=candidate_id)
        return kwargs

class sec_edit_journal(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    model = JournalPublication
    template_name = "phds/sec_edit_journal.html"
    form_class = SecEditJournalForm
    # success_url = reverse_lazy('phds:sec_list_journals')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["candidate"] = self.object.candidate
    #     return kwargs

@login_required
@user_passes_test(is_secreteriat)
def sec_delete_journal(request, pk):
    obj = get_object_or_404(JournalPublication, pk=pk)
    candidate = obj.candidate    
    obj.delete()
    if candidate:
        return redirect('myprofile:sec_edit_phd_student', pk=candidate.id)
    else:
        return redirect(request.META.get('HTTP_REFERER'))
    
    
    # Conferences

# class sec_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
#     template_name = "phds/sec_list_conferences.html"
#     context_object_name = "conferences"

#     def test_func(self):
#         return is_secreteriat(self.request.user)
    
#     def get_queryset(self):
#         return ConferencePublication.objects.all()
    
class sec_create_conference(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    model = ConferencePublication
    template_name = "phds/sec_edit_conference.html"
    form_class = SecCreateConferenceForm
    # success_url = reverse_lazy('phds:sec_list_conferences')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        candidate_id = self.kwargs.get("pk")
        kwargs["candidate"] = get_object_or_404(PhdStudent, id=candidate_id)
        return kwargs

class sec_edit_conference(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    model = ConferencePublication
    template_name = "phds/sec_edit_conference.html"
    form_class = SecEditConferenceForm
    # success_url = reverse_lazy('phds:sec_list_conferences')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["candidate"] = self.object.candidate
    #     return kwargs

@login_required
@user_passes_test(is_secreteriat)
def sec_delete_conference(request, pk):
    obj = get_object_or_404(ConferencePublication, pk=pk)
    candidate = obj.candidate    
    obj.delete()
    if candidate:
        return redirect('myprofile:sec_edit_phd_student', pk=candidate.id)
    else:
        return redirect(request.META.get('HTTP_REFERER'))


    # Teaching

# class sec_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
#     template_name = "phds/sec_list_teachings.html"
#     context_object_name = "teachings"

#     def test_func(self):
#         return is_secreteriat(self.request.user)
    
#     def get_queryset(self):
#         return Teaching.objects.all()

class sec_create_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    model = Teaching
    template_name = "phds/sec_edit_teaching.html"
    form_class = SecCreateTeachingForm
    # success_url = reverse_lazy('phds:sec_list_teachings')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        candidate_id = self.kwargs.get("pk")
        kwargs["candidate"] = get_object_or_404(PhdStudent, id=candidate_id)
        return kwargs

class sec_edit_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    model = Teaching
    template_name = "phds/sec_edit_teaching.html"
    form_class = SecEditTeachingForm
    # success_url = reverse_lazy('phds:sec_list_teachings')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
    def get_success_url(self):
        candidate = self.object.candidate
        if candidate:
            return reverse("myprofile:sec_edit_phd_student", kwargs={"pk": candidate.id})
        else:
            previous_url = self.request.META.get("HTTP_REFERER")
            return previous_url
        
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["candidate"] = self.object.candidate
    #     return kwargs

@login_required
@user_passes_test(is_secreteriat)
def sec_delete_teaching(request, pk):
    obj = get_object_or_404(Teaching, pk=pk)
    candidate = obj.candidate    
    obj.delete()
    if candidate:
        return redirect('myprofile:sec_edit_phd_student', pk=candidate.id)
    else:
        return redirect(request.META.get('HTTP_REFERER'))