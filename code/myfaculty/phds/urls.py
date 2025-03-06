from django.urls import path

from . import views

app_name = 'phds'
urlpatterns = [
    path('sec/phd/journals', views.sec_list_journals.as_view(), name='sec_list_journals'),
    path('sec/phd/conferences', views.sec_list_conferences.as_view(), name='sec_list_conferences'),
    path('sec/phd/teachings', views.sec_list_teachings.as_view(), name='sec_list_teachings'),

    path('staff/phd/journals', views.staff_list_journals.as_view(), name='staff_list_journals'),
    path('staff/phd/conferences', views.staff_list_conferences.as_view(), name='staff_list_conferences'),
    path('staff/phd/teachings', views.staff_list_teachings.as_view(), name='staff_list_teachings'),

    path('phd/journals', views.phd_list_journals.as_view(), name='phd_list_journals'),
    path('phd/conferences', views.phd_list_conferences.as_view(), name='phd_list_conferences'),
    path('phd/teachings', views.phd_list_teachings.as_view(), name='phd_list_teachings')
]