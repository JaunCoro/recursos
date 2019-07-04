from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Songs, Categoria, Material, Request

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("pk", "name")
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ("pk", "name", "categoria", "disponibilidad", "img")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.categoria = validated_data.get("categoria", instance.categoria)
        instance.disponibilidad = validated_data.get("disponibilidad", instance.disponibilidad)
        instance.img = validated_data.get("img", instance.img)
        instance.save()
        return instance

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("user", "material", "uso", "salida")
    
    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.material = validated_data.get("material", instance.material)
        instance.uso = validated_data.get("uso", instance.uso)
        instance.salida = validated_data.get("salida", instance.salida)
        instance.save()
        return instance

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.artist = validated_data.get("artist", instance.artist)
        instance.save()
        return instance


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance