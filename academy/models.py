from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=11,blank=False,null=False)
    email = models.EmailField(max_length=150,blank=False,null=False)
    designation = models.CharField(max_length=200,blank=False,null=False)
    faculty = models.CharField(max_length=200,blank=False,null=False)
    department = models.CharField(max_length=200,blank=False,null=False)
    priority = models.IntegerField(blank=False,null=False)
    
class DeanOffice(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=11,blank=False,null=False)
    email = models.EmailField(max_length=150,blank=False,null=False)
    designation = models.CharField(max_length=200,blank=False,null=False)
    faculty = models.CharField(max_length=200,blank=False,null=False)
    priority = models.IntegerField(blank=False,null=False)
    
class Staff(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=11,blank=False,null=False)
    email = models.EmailField(max_length=150,blank=False,null=False)
    designation = models.CharField(max_length=200,blank=False,null=False)
    faculty = models.CharField(max_length=200,blank=False,null=False)
    department = models.CharField(max_length=200,blank=False,null=False)
    priority = models.IntegerField(blank=False,null=False)
    
class StudentCR(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=11,blank=False,null=False)
    email = models.EmailField(max_length=150,blank=False,null=False)
    faculty = models.CharField(max_length=200,blank=False,null=False)
    semester = models.IntegerField(blank=False,null=False)
    
def __str__(self):
    return self.name
    