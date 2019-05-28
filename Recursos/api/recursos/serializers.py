from rest_framework import serializers
from recursos.models import User, Materiales

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User
        fields = ('url', 'name', 'matricula', 'correo', 'rol')

class MaterialesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materiales
        fields = ('url', 'name', 'disponibilidad', 'apartado', 'categoria')