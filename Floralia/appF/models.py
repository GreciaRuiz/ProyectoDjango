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
	password= models.CharField(max_length=40)

	class Meta:
		verbose_name_plural: 'Usuarios'
	
	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre= models.CharField(max_length=50)
	descrip= models.CharField(max_length=100)
	stock= models.IntegerField(max_length=5)
	precio= models.IntegerField(max_length=6)
	
	class Meta:
		verbose_name_plural: 'Productos'

	def __str__(self):
		return self.nombre

class TipoUno(models.Model):
	tipoP= models.CharField(max_length=10)

	class Meta:
		verbose_name_plural: 'TipoProd'

	def __str__(self):
		return self.TipoP

class TipoDos(models.Model):
	tipoD= models.CharField(max_length=10)

	class Meta:
		verbose_name_plural: 'TipoDosProd'

	def __str__(self):
		return self.tipoD
# Create your models here.
