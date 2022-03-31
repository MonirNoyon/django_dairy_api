from dataclasses import fields
from operator import mod
from . models import Administration
from rest_framework import serializers

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'