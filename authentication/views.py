from django.shortcuts import render, redirect
from .models import CustomUser
from rest_framework import generics
from .serializers import AllUserSerializer, DetailUserSerializer


class CreateCustomUserView(generics.CreateAPIView):
    serializer_class = DetailUserSerializer
    

class AllCustomUserView(generics.ListAPIView):
    serializer_class = AllUserSerializer
    queryset = CustomUser.get_all()

class DetailCustomUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailUserSerializer
    queryset = CustomUser.get_all()