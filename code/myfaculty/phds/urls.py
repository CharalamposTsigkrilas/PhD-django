from django.urls import path
from . import views

app_name = 'phds'
urlpatterns = [
    path('sec/journal/<int:pk>', views.sec_edit_journal.as_view(), name='sec_edit_journal'),
    path('sec/journal/<int:pk>/delete', views.sec_delete_journal, name='sec_delete_journal'),
    path('sec/phd/<int:pk>/journal/new', views.sec_create_journal.as_view(), name='sec_create_journal'),

    path('sec/conference/<int:pk>', views.sec_edit_conference.as_view(), name='sec_edit_conference'),
    path('sec/conference/<int:pk>/delete', views.sec_delete_conference, name='sec_delete_conference'),
    path('sec/phd/<int:pk>/conference/new', views.sec_create_conference.as_view(), name='sec_create_conference'),

    path('sec/teaching/<int:pk>', views.sec_edit_teaching.as_view(), name='sec_edit_teaching'),
    path('sec/teaching/<int:pk>/delete', views.sec_delete_teaching, name='sec_delete_teaching'),
    path('sec/phd/<int:pk>/teaching/new', views.sec_create_teaching.as_view(), name='sec_create_teaching'),

    
    path('staff/journal/<int:pk>/details', views.staff_spectate_journal.as_view(), name='staff_spectate_journal'),
    
    path('staff/conference/<int:pk>/details', views.staff_spectate_conference.as_view(), name='staff_spectate_conference'),
    
    path('staff/teaching/<int:pk>/details', views.staff_spectate_teaching_accept_reject.as_view(), name='staff_spectate_teaching_accept_reject'),
    path('staff/teachings', views.staff_list_teachings.as_view(), name='staff_list_teachings'),
    path('staff/teachings/teaching/<int:pk>/details', views.staff_spectate_teaching_accept_reject_from_list.as_view(), name='staff_spectate_teaching_accept_reject_from_list'),

    
    path('phd/journals', views.phd_list_journals.as_view(), name='phd_list_journals'),
    path('phd/journal/<int:pk>/details', views.phd_spectate_journal.as_view(), name='phd_spectate_journal'),
    path('phd/journal/new', views.phd_create_journal.as_view(), name='phd_create_journal'),
    
    path('phd/conferences', views.phd_list_conferences.as_view(), name='phd_list_conferences'),
    path('phd/conference/<int:pk>/details', views.phd_spectate_conference.as_view(), name='phd_spectate_conference'),
    path('phd/conference/new', views.phd_create_conference.as_view(), name='phd_create_conference'),
    
    path('phd/teachings', views.phd_list_teachings.as_view(), name='phd_list_teachings'),
    path('phd/teaching/<int:pk>/details', views.phd_spectate_teaching.as_view(), name='phd_spectate_teaching'),
    path('phd/teaching/new', views.phd_create_teaching.as_view(), name='phd_create_teaching'),
]