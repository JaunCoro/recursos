from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.parsers import FileUploadParser

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .decorators import validate_request_data, validate_categoria_data, validate_material_data, validate_request
from .models import Songs, Material, Categoria, Request
from .serializers import CategoriaSerializer, MaterialSerializer, RequestSerializer, SongsSerializer, TokenSerializer, UserSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_user = self.queryset.get(username=kwargs["username"])
            return Response(UserSerializer(a_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    "message": "Categoria with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class ListCreateCategoriasView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_categoria_data
    def post(self, request, *args, **kwargs):
        a_categoria = Categoria.objects.create(
            name=request.data["name"]
        )
        return Response(
            data=CategoriaSerializer(a_categoria).data,
            status=status.HTTP_201_CREATED
        )

class CategoriasDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_categoria = self.queryset.get(pk=kwargs["pk"])
            return Response(CategoriaSerializer(a_categoria).data)
        except Categoria.DoesNotExist:
            return Response(
                data={
                    "message": "Categoria with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_categoria_data
    def put(self, request, *args, **kwargs):
        try:
            a_categoria = self.queryset.get(pk=kwargs["pk"])
            serializer = CategoriaSerializer()
            updated_cat = serializer.update(a_categoria, request.data)
            return Response(CategoriaSerializer(updated_cat).data)
        except Categoria.DoesNotExist:
            return Response(
                data={
                    "message": "Categoria with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_categoria = self.queryset.get(pk=kwargs["pk"])
            a_categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response(
                data={
                    "message": "Categoria with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ListCreateMaterialView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    parser_classes = (FileUploadParser,)
    permission_classes = (permissions.IsAuthenticated,)

    @validate_material_data
    def post(self, request, *args, **kwargs):
        a_material = Material.objects.create(
            name=request.data["name"],
            categoria=Categoria.objects.get(pk = int(request.data["categoria"])),
            img= request.data["img"]
        )
        return Response(
            data=MaterialSerializer(a_material).data,
            status=status.HTTP_201_CREATED
        )

class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            return Response(MaterialSerializer(a_material).data)
        except Material.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    @validate_material_data
    def put(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            serializer = MaterialSerializer()
            updated_material = serializer.update(a_material, request.data)
            return Response(MaterialSerializer(updated_material).data)
        except Material.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, *args, **kwargs):
        try:
            a_material = self.queryset.get(pk=kwargs["pk"])
            a_material.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Material.DoesNotExist:
            return Response(
                data={
                    "message": "Material with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ListCreateRequest(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request
    def post(self, request, *args, **kwargs):
        a_request = Request.objects.create(
            user=User.objects.get(pk = int(request.data["user"])),
            material=Material.objects.get(pk = int(request.data["material"])),
            uso=request.data["uso"]
        )
        return Response(
            data=RequestSerializer(a_request).data,
            status=status.HTTP_201_CREATED
        )

class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            return Response(RequestSerializer(a_request).data)
        except Request.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
    @validate_request
    def put(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            serializer = RequestSerializer()
            updated_song = serializer.update(a_request, request.data)
            return Response(RequestSerializer(updated_song).data)
        except Request.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            a_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Request.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ListCreateSongsView(generics.ListCreateAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_song = Songs.objects.create(
            title=request.data["title"],
            artist=request.data["artist"]
        )
        return Response(
            data=SongsSerializer(a_song).data,
            status=status.HTTP_201_CREATED
        )


class SongsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET songs/:id/
    PUT songs/:id/
    DELETE songs/:id/
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            return Response(SongsSerializer(a_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            serializer = SongsSerializer()
            updated_song = serializer.update(a_song, request.data)
            return Response(SongsSerializer(updated_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            a_song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """

    # This permission class will over ride the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )
