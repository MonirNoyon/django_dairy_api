from telnetlib import STATUS
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import DeanOfficeSerializer, TeacherSerializer,StaffSerializer,StudentCRSerializer
from .models import DeanOffice, Teacher,Staff,StudentCR
# Create your views here.


@api_view(['GET'])
def showTeacher(request):
    teachers = Teacher.objects.all()
    serializers = TeacherSerializer(teachers,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def showFacultyTeacher(request):
    faculty = request.POST['faculty']
    teacher = Teacher.objects.filter(faculty = faculty)
    serializers = TeacherSerializer(teacher,many= True)
    return Response(serializers.data)

@api_view(['GET'])
def showAllDeanOffice(request):
    deans = DeanOffice.objects.all()
    serializers = DeanOfficeSerializer(deans,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def showFacultyDean(request):
    faculty = request.POST['faculty']
    deans = DeanOffice.objects.filter(faculty = faculty)
    serializers = DeanOfficeSerializer(deans,many= True)
    return Response(serializers.data)


@api_view(['GET'])
def showAllStaff(request):
    staffs = Staff.objects.all()
    serializers = StaffSerializer(staffs,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def showFacultyStaff(request):
    faculty = request.POST['faculty']
    staffs = Staff.objects.filter(faculty = faculty)
    serializers = StaffSerializer(staffs,many= True)
    return Response(serializers.data)

@api_view(['GET'])
def showAllStudenCR(request):
    students = StudentCR.objects.all()
    serializers = StudentCRSerializer(students,many = True)
    return Response(serializers.data)

@api_view(['POST'])
def showFacultyStudentCR(request):
    faculty = request.POST['faculty']
    student = StudentCR.objects.filter(faculty = faculty)
    serializers = StudentCRSerializer(student,many= True)
    return Response(serializers.data)
