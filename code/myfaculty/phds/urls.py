from django.urls import path
from . import views

app_name = 'phds'
urlpatterns = [
    path('sec/journals', views.sec_list_journals.as_view(), name='sec_list_journals'),
    path('sec/conferences', views.sec_list_conferences.as_view(), name='sec_list_conferences'),
    path('sec/teachings', views.sec_list_teachings.as_view(), name='sec_list_teachings'),

    path('staff/journals', views.staff_list_journals.as_view(), name='staff_list_journals'),
    # path('staff/journals/phd/<int:pk>', views.staff_list_journals, name='staff_list_journals'),
    path('staff/conferences', views.staff_list_conferences.as_view(), name='staff_list_conferences'),
    path('staff/teachings', views.staff_list_teachings.as_view(), name='staff_list_teachings'),

    path('phd/journals', views.phd_list_journals.as_view(), name='phd_list_journals'),
    path('phd/conferences', views.phd_list_conferences.as_view(), name='phd_list_conferences'),
    path('phd/teachings', views.phd_list_teachings.as_view(), name='phd_list_teachings'),
]