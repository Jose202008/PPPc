from django.db import models

# Create your models here.
class Usuarios(models.Model):
	Apellido = models.CharField(max_length=30)
	Nombre = models.CharField(max_length=30)
	DNI = models.CharField(max_length=8)
	FechaNac = models.DateField()
	Sexos = (("F",'Femenino'), ("M",'Masculino'), ("O",'Otro'))
	Sexo = models.CharField(max_length=1, choices=Sexos, default="M")
	Bloqueado = models.BooleanField(default=False)

	def __str__(self):
		return ('{0}, {1} DNI {2}'.format (self.Apellido, self.Nombre, self.DNI))
