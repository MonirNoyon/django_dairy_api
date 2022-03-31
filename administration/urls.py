from django.urls import path
from . import views

urlpatterns = [
    path('',views.showAllAdministration,name='show_all_administration'),
    path('all/',views.showAdministration,name='show_administration'),
]
