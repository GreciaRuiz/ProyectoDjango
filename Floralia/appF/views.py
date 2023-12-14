from django.shortcuts import render, HttpResponse
from .models import *

def inicio(request):
	return render (request,"index.html")

def registro(request):
	return render (request,"registro.html")
	
def plantas(request):
	return render (request,"plantas.html")

def macetas(request):
	return render (request, "macetas.html")

def login(request):
	return render (request, "login.html")

def proveedores(request):
	proveedores=Proveedor.objects.all()
	p={'proveedores':proveedores}
	return render(request, 'proveedores.html', p)

def detalle(request):
	return render (request, "detalle.html")
# Create your views here.

