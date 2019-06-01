from rest_framework import serializers
from recursos.models import User, Materiales

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User
        fields = ('url', 'name', 'matricula', 'correo', 'rol')

class MaterialesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Materiales
        fields = ('url', 'name', 'categoria', 'disponibilidad', 'apartado', 'img')

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.categoria = validated_data.get("categoria", instance.categoria)
        instance.disponibilidad = validated_data.get("disponibilidad", instance.disponibilidad)
        instance.apartado = validated_data.get("apartado", instance.apartado)
        instance.img = validated_data.get("img", instance.img)
        instance.save()
        return instance