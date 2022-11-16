from rest_framework import serializers
from django.contrib.auth.models import User
from employes.serializers import EmployeSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = EmployeSerializer()
    class Meta:
        model = User
        fields = ('pk', 'username', 'profile')

    def update(self, instance, validated_data):
        # profile
        profile_validated_data = validated_data.pop('profile', None)
        profile = instance.profile                    
        profile.emp_phone = profile_validated_data.get('emp_phone', profile.emp_phone)
        profile.emp_gender = profile_validated_data.get('emp_gender', profile.emp_gender)
        profile.emp_marital = profile_validated_data.get('emp_marital', profile.emp_marital)
        profile.save()

        # user
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        return instance