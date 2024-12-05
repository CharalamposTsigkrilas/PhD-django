from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from myprofile.checks import is_staff_member, is_secreteriat
from .models import Thesis
from myprofile.models import StaffMember
from curricula.models import StudyProgram
from .forms import SecCreateForm, SecUpdateForm, StaffCreateForm, StaffUpdateForm, PublicDetailForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
import csv

# Create your views here.

@login_required
@user_passes_test(is_secreteriat)
def sec_list(request):

    theses_assigned = Thesis.objects.filter(assigned_to__isnull = False).order_by('-updated_date')
    theses_unassigned = Thesis.objects.filter(assigned_to__isnull = True).order_by('-updated_date')
    programs = StudyProgram.objects.all()
    return render(request, 'theses/sec_list.html', context = {
      'theses_assigned' : theses_assigned,
      'theses_unassigned' : theses_unassigned,
      'programs' : programs
    })

def sec_list_program(request, id):
    program = get_object_or_404(StudyProgram, pk=id)
    theses = Thesis.objects.filter(offered_in = program)
    theses_assigned = theses.filter(assigned_to__isnull = False, grade_avg__isnull=True).order_by('-updated_date')
    theses_unassigned = Thesis.objects.filter(assigned_to__isnull = True).order_by('-updated_date')
    theses_grade = theses.filter(grade_avg__isnull = False).order_by('-updated_date')

    return render(request, 'theses/sec_program_list.html', context = {
      'theses_assigned' : theses_assigned,
      'theses_unassigned' : theses_unassigned,
      'theses_grade' : theses_grade,
      'program' : program
    })

class sec_edit(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Thesis
    template_name = "theses/sec_edit.html"
    form_class = SecUpdateForm
    success_url = reverse_lazy('theses:sec_list')

    def test_func(self):
        return is_secreteriat(self.request.user)
    
class sec_create(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):
    model = Thesis
    template_name = "theses/sec_edit.html"
    form_class = SecCreateForm
    success_url = reverse_lazy('theses:sec_list')

    def test_func(self):
        return is_secreteriat(self.request.user)

@login_required
@user_passes_test(is_secreteriat)    
def sec_delete(request, pk):
    obj = get_object_or_404(Thesis, pk=pk)
    obj.delete()
    return redirect('theses:sec_list')


@login_required
@user_passes_test(is_staff_member)
def staff_list(request):
    P = get_object_or_404(StaffMember, user = request.user)
    theses_active = Thesis.objects.filter(supervisor=P, assigned_to__isnull = True,is_offered=True).order_by('-updated_date')
    theses_inactive = Thesis.objects.filter(supervisor=P,is_offered=False).order_by('-updated_date')
    theses_assigned = Thesis.objects.filter(supervisor=P, assigned_to__isnull = False).order_by('-updated_date')
    theses_member = Thesis.objects.filter( Q(member1=P) | Q(member2=P) ).order_by('-updated_date')
    print(theses_member)
    return render(request, 'theses/staff_list.html', context={'theses_active' : theses_active,
                                                              'theses_assigned' : theses_assigned,
                                                              'theses_member' : theses_member,
                                                              'theses_inactive' : theses_inactive})

class staff_edit(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Thesis
    template_name = "theses/staff_edit.html"
    form_class = StaffUpdateForm
    success_url = reverse_lazy('theses:staff_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        
        # Changes can not be made if the thesis is assigned 
        P = get_object_or_404(StaffMember, user = self.request.user)
        if form.instance.supervisor == P:
            pass
        elif form.instance.assigned_to or form.instance.member1==P or form.instance.member2==P:
            #form.fields.pop('assigned_to_char')
            for f in form.fields:
                form.fields[f].disabled = True
                
        # Check fields that need to be activated
        if form.instance.supervisor == P:
            form.fields['grade_sup'].disabled = False
        elif form.instance.member1 == P:
            form.fields['grade_member1'].disabled = False
        elif form.instance.member2 == P:
            form.fields['grade_member2'].disabled = False
            
        return form
    
    def test_func(self):
        obj = self.get_object()        
        return is_staff_member(self.request.user) and ( 
                (obj.supervisor.user == self.request.user) 
                or (obj.member1.user == self.request.user)                     
                or (obj.member2.user == self.request.user) )
    
@login_required
@user_passes_test(is_staff_member)
def staff_create(request):
    supervisor = get_object_or_404(StaffMember, user=request.user)
    if request.method == 'POST':
        form = StaffCreateForm(request.POST, request.FILES)

        if form.is_valid():
            print(form)
            obj = form.save(commit=False)
            obj.supervisor = supervisor
            obj.save()
            return redirect('theses:staff_list')
        print(form.errors)
    else:
        form = StaffCreateForm()

    return render(request, 'theses/staff_edit.html', {'form' : form})

@login_required
def staff_delete(request, pk):
    p = get_object_or_404(StaffMember, user = request.user)
    obj = get_object_or_404(Thesis, pk=pk, supervisor = p)
    obj.delete()
    return redirect('theses:staff_list')


@login_required
@user_passes_test(is_secreteriat)
def cancel_assignment(request, pk):
    obj = get_object_or_404(Thesis, pk=pk)
    obj.assigned_to_char = None
    obj.assigned_to = None
    obj.assignment_date = None
    
    obj.save()
    return redirect('theses:sec_list')

def public_list(request,c):
    
    P = get_object_or_404(StudyProgram, code_gr=str(c))
    theses = Thesis.objects.filter(is_offered = True, offered_in= P).order_by('-created_date')
    return render(request, 'theses/public_list.html', context={'theses' : theses, 'program' : P})

def public_detail(request,pk):    
    
    thesis = get_object_or_404(Thesis, pk = pk, is_offered=True)
    form = PublicDetailForm(instance=thesis)
    return render(request, 'theses/public_detail.html', context={'form' : form})


def objs_to_csv(objs):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="export.csv"'},
    )

    writer = csv.writer(response, delimiter=';', quoting = csv.QUOTE_ALL)        
    i = 0
    for obj in objs:
        try:
            d = {
                'supervisor_id': obj.supervisor.display_name,
                'member1_id': obj.member1.display_name,
                'member2_id': obj.member2.display_name,
                'title_gr': obj.title_gr,
                'title_en': obj.title_en,
                'abstract': obj.abstract,
                'updated_date': obj.updated_date,
                'created_date': obj.created_date,
                'is_offered': obj.is_offered,
                'assigned_to_id': obj.assigned_to.display_name,
                'assigned_reg' : obj.assigned_to.reg_num,
                'assigned_email' : obj.assigned_to.email,
                'assignment_ga': obj.assignment_ga,
                'assignment_date': obj.assignment_date,
                'notes': obj.notes,
                'grade_sup': obj.grade_sup,
                'grade_member1': obj.grade_member1,
                'grade_member2': obj.grade_member2,
                'grade_avg': obj.grade_avg
                }
                
            if i==0:
                writer.writerow(d.keys())
            l = [d[k] for k in d.keys()]
            i += 1
            writer.writerow(l)
        except AttributeError:
            pass

    return response

@login_required
@user_passes_test(is_secreteriat)
def export_non_ga(request):

    objs= Thesis.objects.filter(assigned_to__isnull = False, assignment_ga__isnull = True).order_by('-updated_date')
    return objs_to_csv(objs)

@login_required
@user_passes_test(is_secreteriat)        
def export_graded_program(request, id):

    program = get_object_or_404(StudyProgram, pk = id)
    objs= Thesis.objects.filter(grade_avg__isnull = False, offered_in = program).order_by('-updated_date')
    return objs_to_csv(objs)
