from django.contrib import admin
from . models import Teacher,DeanOffice,Staff,StudentCR

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','email','designation','faculty','department','priority']
    ordering = ['priority']
    #actions = [make_published]

class DeanAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','email','designation','faculty','priority']
    ordering = ['priority']
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','email','designation','faculty','department','priority']
    ordering = ['priority']
    
    
class StudentCRAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','email','faculty','semester']
    ordering = ['semester']
    

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(DeanOffice,DeanAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(StudentCR,StudentCRAdmin)