from django.contrib import admin
from . models import Administration

# Register your models here.
class AdministrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','email','designation','department','faculty','priority']
    ordering = ['priority']
    

admin.site.register(Administration,AdministrationAdmin)
