from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

# Create your views here.


# phds views --> PhD students create and spectate only
        
    # Journals

class phd_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    def dummy():
        return

class phd_create_journal(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return
    
class phd_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return
    
    
    # Conferences

class phd_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return

class phd_create_conference(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return
    
class phd_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return  
    
    
    # Teachings

class phd_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return

class phd_create_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return
    
class phd_spectate_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return




# staff views --> Staff Members spectate only and accepting/rejecting Teaching --> Only for the PhDs they have.
    
    # Journals

class staff_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    def dummy():
        return

class staff_spectate_journal(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return
    
    
    # Conferences

class staff_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return

class staff_spectate_conference(UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):   
    def dummy():
        return    
    
    
    # Teaching

class staff_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return

class staff_spectate_accept_reject_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return
    


# sec views --> Secreatary CRUD everything
    
    # Journals

class sec_list_journals(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):   
    def dummy():
        return

class sec_create_journal(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return

class sec_update_journal(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_journal():
    return
    
    
    # Conferences

class sec_list_conferences(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return
    
class sec_create_conference(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return

class sec_update_conference(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_conference():
    return


    # Teaching

class sec_list_teachings(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    def dummy():
        return

class sec_create_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.CreateView):   
    def dummy():
        return

class sec_update_teaching(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):   
    def dummy():
        return

def sec_delete_teaching():
    return