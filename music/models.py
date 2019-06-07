from django.db import models
from django.contrib.auth.models import User
import datetime


class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)

class Categoria(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return "{}".format(self.name)

class Material(models.Model):
    name = models.CharField(max_length = 100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default = True)
    img = models.CharField(max_length = 150)
    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.categoria, self.disponibilidad, self.img)

class Request(models.Model):
    #constantes
    EXTERNO = 'EX'
    INTERNO = 'IN'
    USO = (
        (EXTERNO, 'Externo'),
        (INTERNO, 'Interno')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    uso = models.CharField(max_length = 2, choices = USO, default = INTERNO)
    salida = models.CharField(max_length = 150, default = datetime.datetime.now())

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user, self.material, self.uso, self.salida)
