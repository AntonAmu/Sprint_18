from rest_framework import serializers
from .models import Book
from django.core.exceptions import ValidationError

class AllBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'

class DetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'