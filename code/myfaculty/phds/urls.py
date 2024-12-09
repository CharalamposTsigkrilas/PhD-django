from django.urls import path
from . import views

app_name = 'phds'
urlpatterns = [
    path('sec/phd/new', views.sec_create_phd_student.as_view(), name='sec_create_phd_student'),
    path('sec/phds', views.sec_list_phd_students.as_view(), name='sec_list_phd_students'),
    path('sec/phd/<int:pk>', views.sec_edit_phd_student.as_view(), name='sec_edit_phd_student'),
    path('sec/phd/<int:pk>/delete', views.sec_delete_phd_student.as_view(), name='sec_delete_phd_student'),
    path('staff/phds', views.staff_list_phd_students.as_view(), name='staff_list_phd_students'),
    path('phd/<int:pk>/profile', views.phd_student_profile.as_view(), name='phd_student_profile'),
    path('phd/<int:pk>', views.phd_student_edit.as_view(), name='phd_student_edit'),
]