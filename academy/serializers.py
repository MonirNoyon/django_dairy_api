from rest_framework import serializers
from .models import Teacher,DeanOffice,Staff,StudentCR

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
    

class DeanOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeanOffice
        fields = '__all__'
        

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        

class StudentCRSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCR
        fields = '__all__'