from django.shortcuts import render, get_object_or_404, redirect
from myprofile.checks import is_staff_member, is_secreteriat
from .models import Timesheet
from myprofile.models import StaffMember
from .forms import SecCreateForm, SecUpdateForm, StaffCreateForm, StaffUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

class sec_list(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "timesheets/sec_list.html"
    context_object_name = "timesheets"

    def test_func(self):
        return is_secreteriat(self.request.user)

    def get_queryset(self):
        return Timesheet.objects.order_by('-created_date')

class sec_edit(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Timesheet
    template_name = "timesheets/sec_edit.html"
    form_class = SecUpdateForm
    success_url = reverse_lazy('timesheets:sec_list')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
class sec_create(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = Timesheet
    template_name = "timesheets/sec_edit.html"
    form_class = SecCreateForm
    success_url = reverse_lazy('timesheets:sec_list')

    def test_func(self):
        return is_secreteriat(self.request.user)

@login_required
@user_passes_test(is_secreteriat)    
def sec_delete(request, pk):
    obj = get_object_or_404(Timesheet, pk=pk)
    obj.delete()
    return redirect('timesheets:sec_list')

class staff_list(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "timesheets/staff_list.html"
    context_object_name = "timesheets"

    def test_func(self):
        return is_staff_member(self.request.user)

    def get_queryset(self):
        P = get_object_or_404(StaffMember, user = self.request.user)
        return Timesheet.objects.filter(applicant=P).order_by('-created_date')

class staff_edit(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Timesheet
    template_name = "timesheets/staff_edit.html"
    form_class = StaffUpdateForm
    success_url = reverse_lazy('timesheets:staff_list')

    def test_func(self):
        obj = self.get_object()        
        return is_staff_member(self.request.user) and (obj.applicant.user == self.request.user)
    
@login_required
@user_passes_test(is_staff_member)
def staff_create(request):
    applicant = get_object_or_404(StaffMember, user=request.user)
    if request.method == 'POST':
        form = StaffCreateForm(request.POST, request.FILES)

        if form.is_valid():
            print(form)
            obj = form.save(commit=False)
            obj.applicant = applicant
            obj.save()
            return redirect('timesheets:staff_list')
        print(form.errors)
    else:
        form = StaffCreateForm()

    return render(request, 'timesheets/staff_edit.html', {'form' : form})

@login_required
def staff_delete(request, pk):
    p = get_object_or_404(StaffMember, user = request.user)
    obj = get_object_or_404(Timesheet, pk=pk, applicant = p)
    obj.delete()
    return redirect('timesheet:staff_list')
