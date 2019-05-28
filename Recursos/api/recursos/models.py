from django.db import models
import datetime

# Create your models here.
class User(models.Model):
	def __str__(self):
		return self.name
	#Constantes en el modelo
	ALUMNO = 'AL'
	MAESTRO = 'MA'
	Rol_CHOICES = (
		(MAESTRO, 'Maestro'),
		(ALUMNO, 'Alumno'),
	)
	name = models.CharField(max_length = 50)
	matricula = models.CharField(max_length = 100)
	correo = models.EmailField(max_length = 254)
	password = models.CharField(max_length = 100, default='')
	rol = models.CharField(max_length = 2, choices = Rol_CHOICES, default=ALUMNO)

class Categoria(models.Model):
	name = models.CharField(max_length = 50)

class Materiales(models.Model):
	#Constantes del modelo
	name = models.CharField(max_length = 100)
	categoria = models.CharField(max_length = 50)
	disponibilidad = models.BooleanField(default=True)
	apartado = models.BooleanField(default=False)
	img = models.CharField(max_length = 50, default="img.png")

	def __str__(self):
		return "{} - {}".format(self.name, self.categoria)

class Solicitudes(models.Model):
	solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_salida = models.DateField(default = datetime.date.today)
	hora_salida = models.TimeField(default = datetime.time)
	fecha_entrada = models.DateField()
	hora_entrada = models.TimeField()