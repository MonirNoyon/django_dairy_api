from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CourseSerializers
from .models import Course

# Create your views here.

@api_view(['GET'])
def showCourse(request):
    faculty = request.POST['faculty']
    teacher = Course.objects.filter(faculty = faculty)
    serializers = CourseSerializers(teacher,many= True)
    return Response(serializers.data)