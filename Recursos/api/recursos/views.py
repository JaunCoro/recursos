from django.shortcuts import get_object_or_404
from recursos.models import Materiales, User
from rest_framework import generics
from recursos.serializers import UserSerializer, MaterialesSerializer
# Create your views here.

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class MaterialViewSet(generics.ListCreateAPIView):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj  = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj