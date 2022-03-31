from django.urls import path
from  . import views

urlpatterns = [
    path('',views.showCourse,name="show_course"),
]
