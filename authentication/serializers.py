from rest_framework import serializers
from .models import CustomUser 
from django.core.exceptions import ValidationError

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =('id', 'first_name', 'last_name', 'email', 'middle_name', 'password', 'role', 'is_active')


class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'
        read_only_fields = ('last_login', 'id', 'updated_at', 'created_at', 'role')

