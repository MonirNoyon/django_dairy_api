from django.db import models

# Create your models here.

class Course(models.Model):
    c_title = models.CharField(max_length=200,blank=False,null=False)
    c_code = models.CharField(max_length=200,blank=False,null=False)
    c_hour = models.IntegerField(blank=False,null=False)
    faculty = models.CharField(max_length=200,blank=False,null=False)
    semister = models.CharField(max_length=200,blank=False,null =False)
    
def __str__(self):
    return self.title
