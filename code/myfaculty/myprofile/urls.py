from django.urls import path

from . import views

app_name = 'myprofile'
urlpatterns = [
    path("", views.index, name="index"),
    path('logout', views.logout_view, name='logout'),
    path('sec/associates', views.list_associates.as_view(), name='list_associates'),
    path('sec/associate/<int:pk>', views.edit_associate.as_view(), name='edit_associate'),
    path('sec/associate/<int:pk>/delete', views.delete_associate, name='delete_associate'),
    path('sec/associates/new', views.create_associate.as_view(), name='create_associate'),    
    
    path('sec/staff', views.list_staff.as_view(), name='list_staff'),    
    path('sec/staff/<int:pk>', views.edit_staff.as_view(), name='edit_staff'),
    path('sec/staff/<int:pk>/delete', views.delete_staff, name='delete_staff'),
    path('sec/staff/new', views.create_staff.as_view(), name='create_staff'),    
 
    path('staff/associates', views.staff_list_associates.as_view(), name='staff_list_associates'),
    path('staff/associate/<int:pk>', views.staff_edit_associate.as_view(), name='staff_edit_associate'),  
    path('staff/associate/<int:pk>/delete', views.staff_delete_associate, name='staff_delete_associate'),

    path('staffmember-autocomplete/', views.StaffMemberAutocomplete.as_view(), name='staffmember-autocomplete'),
    path('student-autocomplete/', views.StudentAutocomplete.as_view(), name='student-autocomplete'),

    path('sec/phds', views.sec_list_phd_students.as_view(), name='sec_list_phd_students'),
    path('sec/phd/<int:pk>', views.sec_edit_phd_student.as_view(), name='sec_edit_phd_student'),
    path('sec/phd/<int:pk>/delete', views.sec_delete_phd_student, name='sec_delete_phd_student'),
    path('sec/phd/new', views.sec_create_phd_student.as_view(), name='sec_create_phd_student'),
    
    path('staff/phds', views.staff_list_phd_students.as_view(), name='staff_list_phd_students'),
    
]