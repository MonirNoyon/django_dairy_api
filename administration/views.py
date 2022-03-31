from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AdministrationSerializer
from .models import Administration
# Create your views here.


@api_view(['GET'])
def showAllAdministration(request):
    administrations = Administration.objects.all()
    serializers = AdministrationSerializer(administrations,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def showAdministration(request):
    faculty = request.POST['faculty']
    teacher = Administration.objects.filter(faculty = faculty)
    serializers = AdministrationSerializer(teacher,many= True)
    return Response(serializers.data)



