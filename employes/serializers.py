from rest_framework import serializers
from .models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ('emp_phone', 'emp_gender', 'emp_marital')