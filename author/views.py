#from django.shortcuts import render, redirect
from .models import Author
from rest_framework import generics
#from django.views.generic import View
from .serializers import DetailAuthorSerializer


class CreateAuthorView(generics.CreateAPIView):
     serializer_class = DetailAuthorSerializer
    

class AllAuthorView(generics.ListAPIView):
    serializer_class = DetailAuthorSerializer
    queryset = Author.get_all()

class DetailAuthorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailAuthorSerializer
    queryset = Author.get_all()
