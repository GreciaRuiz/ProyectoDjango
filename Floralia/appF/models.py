from django.db import models

class Proveedor(models.Model):
	nombre= models.CharField(max_length=80)
	telefono=models.CharField(max_length=25)
	mail=models.CharField(max_length=50)
	direccion=models.CharField(max_length=80)
	productos=models.CharField(max_length=100)

	class Meta:
		verbose_name_plural: 'Proveedores'

	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	email= models.CharField(max_length=50)
	nombre= models.CharField(max_length=40)
	apellido= models.CharField(max_length=30)
	userName=models.CharField(max_length=70)
	password= models.CharField(max_length=40)

	class Meta:
		verbose_name_plural: 'Usuarios'
	
	def __str__(self):
		return self.userName


# Create your models here.
