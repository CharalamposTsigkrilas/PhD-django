from django.urls import path
from . import views

app_name = 'phds'
urlpatterns = [
    path('sec/journals', views.sec_list_journals.as_view(), name='sec_list_journals'),
    path('sec/journal/<int:pk>', views.sec_edit_journal.as_view(), name='sec_edit_journal'),
    path('sec/journal/<int:pk>/delete', views.sec_delete_journal, name='sec_delete_journal'),
    path('sec/journal/new', views.sec_create_journal.as_view(), name='sec_create_journal'),

    path('sec/conferences', views.sec_list_conferences.as_view(), name='sec_list_conferences'),
    path('sec/conference/<int:pk>', views.sec_edit_conference.as_view(), name='sec_edit_conference'),
    path('sec/conference/<int:pk>/delete', views.sec_delete_conference, name='sec_delete_conference'),
    path('sec/conference/new', views.sec_create_conference.as_view(), name='sec_create_conference'),

    path('sec/teachings', views.sec_list_teachings.as_view(), name='sec_list_teachings'),
    path('sec/teaching/<int:pk>', views.sec_edit_teaching.as_view(), name='sec_edit_teaching'),
    path('sec/teaching/<int:pk>/delete', views.sec_delete_teaching, name='sec_delete_teaching'),
    path('sec/teaching/new', views.sec_create_teaching.as_view(), name='sec_create_teaching'),

    
    # path('staff/journals/phd/<int:pk>', views.staff_list_journals, name='staff_list_journals'),
    path('staff/journals', views.staff_list_journals.as_view(), name='staff_list_journals'),
    path('staff/journal/<int:pk>/details', views.staff_spectate_journal.as_view(), name='staff_spectate_journal'),
    
    path('staff/conferences', views.staff_list_conferences.as_view(), name='staff_list_conferences'),
    path('staff/conference/<int:pk>/details', views.staff_spectate_conference.as_view(), name='staff_spectate_conference'),
    
    path('staff/teachings', views.staff_list_teachings.as_view(), name='staff_list_teachings'),
    path('staff/teaching/<int:pk>/details', views.staff_spectate_teaching_accept_reject.as_view(), name='staff_spectate_teaching_accept_reject'),

    
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