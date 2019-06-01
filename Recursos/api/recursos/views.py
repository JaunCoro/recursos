from django.shortcuts import get_object_or_404
from recursos.models import Materiales, User
from rest_framework import generics
from rest_framework.views import status
from rest_framework.response import Response
from recursos.serializers import UserSerializer, MaterialesSerializer
from recursos.decorators import validate_request_data
# Create your views here.

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class MaterialViewSet(generics.ListCreateAPIView):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_song = Materiales.objects.create(
            title=request.data["name"],
            artist=request.data["Categoria"]
        )
        return Response(
            data=MaterialesSerializer(a_song).data,
            status=status.HTTP_201_CREATED
        )