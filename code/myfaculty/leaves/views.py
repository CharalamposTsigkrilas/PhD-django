from django.shortcuts import render, get_object_or_404, redirect
from myprofile.checks import is_staff_member, is_secreteriat
from .models import Leave
from myprofile.models import StaffMember
from .forms import SecCreateLeaveForm, SecUpdateLeaveForm, StaffCreateLeaveForm, StaffUpdateLeaveForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from export.models import DocumentTemplate
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

class sec_list_leaves(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "leaves/sec_list_leaves.html"
    context_object_name = "leaves"

    def test_func(self):
        return is_secreteriat(self.request.user)

    def get_queryset(self):
        return Leave.objects.order_by('-created_date')

class sec_edit_leave(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Leave
    template_name = "leaves/sec_edit_leave.html"
    form_class = SecUpdateLeaveForm
    success_url = reverse_lazy('leaves:sec_list_leaves')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
class sec_create_leave(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = Leave
    template_name = "leaves/sec_edit_leave.html"
    form_class = SecCreateLeaveForm
    success_url = reverse_lazy('leaves:sec_list_leaves')

    def test_func(self):
        return is_secreteriat(self.request.user)


@login_required
@user_passes_test(is_secreteriat)    
def delete_leave(request, pk):
    obj = get_object_or_404(Leave, pk=pk)
    obj.delete()
    return redirect('leaves:sec_list_leaves')

class staff_list_leaves(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    template_name = "leaves/staff_list_leaves.html"
    context_object_name = "leaves"

    def test_func(self):
        return is_staff_member(self.request.user)

    def get_queryset(self):
        P = get_object_or_404(StaffMember, user = self.request.user)
        return Leave.objects.filter(applicant=P).order_by('-created_date')

class staff_edit_leave(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Leave
    template_name = "leaves/staff_edit_leave.html"
    form_class = StaffUpdateLeaveForm
    success_url = reverse_lazy('leaves:staff_list_leaves')

    def test_func(self):
        obj = self.get_object()        
        return is_staff_member(self.request.user) and (obj.applicant.user == self.request.user)
    
@login_required
@user_passes_test(is_staff_member)
def staff_create_leave(request):
    applicant = get_object_or_404(StaffMember, user=request.user)
    if request.method == 'POST':
        form = StaffCreateLeaveForm(request.POST, request.FILES)

        if form.is_valid():
            print(form)
            obj = form.save(commit=False)
            obj.applicant = applicant
            obj.save()
            return redirect('leaves:staff_list_leaves')
        print(form.errors)
    else:
        form = StaffCreateLeaveForm()

    return render(request, 'leaves/staff_edit_leave.html', {'form' : form})

@login_required
def staff_delete_leave(request, pk):
    p = get_object_or_404(StaffMember, user = request.user)
    obj = get_object_or_404(Leave, pk=pk, applicant = p)
    obj.delete()
    return redirect('leaves:staff_list_leaves')

@login_required
@user_passes_test(is_secreteriat)
def export_leave_approval(request, pk):
    d = DocumentTemplate.objects.get(name=settings.LEAVE_TEMPLATE)
    p = Leave.objects.get(pk = pk)    
    return d.export_file_response(p.approval_dict())