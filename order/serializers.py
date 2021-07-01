from rest_framework import serializers
from .models import Order
from django.core.exceptions import ValidationError

class AllOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'

class DetailOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'