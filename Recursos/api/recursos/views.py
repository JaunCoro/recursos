from django.shortcuts import render
from recursos.models import Materiales, User
from rest_framework import generics
from recursos.serializers import UserSerializer, MaterialesSerializer
# Create your views here.

class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class MaterialViewSet(generics.ListAPIView):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializer 