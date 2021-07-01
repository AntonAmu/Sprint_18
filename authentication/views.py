from django.shortcuts import render, redirect
from .models import CustomUser
from rest_framework import generics
from .serializers import AllUserSerializer, DetailUserSerializer
from order.serializers import AllOrderSerializer
from order.models import Order

class CreateCustomUserView(generics.CreateAPIView):
    serializer_class = DetailUserSerializer
    

class AllCustomUserView(generics.ListAPIView):
    serializer_class = AllUserSerializer
    queryset = CustomUser.get_all()

class DetailCustomUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailUserSerializer
    queryset = CustomUser.get_all()

class OrdersCustomUserView(generics.ListAPIView):
    serializer_class = AllOrderSerializer
    queryset = Order.objects.all()
    
    def get_queryset(self):
        user_pk = self.kwargs['pk']
        return self.queryset.filter(user=user_pk)