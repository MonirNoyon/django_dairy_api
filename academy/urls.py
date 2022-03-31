from django.urls import path
from . import views

urlpatterns = [
    path('',views.showTeacher,name='show_teacher'),
    path('faculty-teacher/',views.showFacultyTeacher,name='faculty_teacher'),
    path('show-all-dean-office/',views.showAllDeanOffice,name='show_dean'),
    path('show-faculty-dean/',views.showFacultyDean,name='show_faculty_dean'),
    path('show-all-staff/',views.showAllStaff,name='show_staff'),
    path('show-faculty-staff/',views.showFacultyStaff,name='show_faculty_staff'),
    path('show-all-studentcr/',views.showAllStudenCR,name='show_studentcr'),
    path('show-faculty-studentcr/',views.showFacultyStudentCR,name='show_faculty_studentcr'),
]
