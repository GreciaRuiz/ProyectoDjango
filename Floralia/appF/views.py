from django.shortcuts import render, HttpResponse

def inicio(request):
	return render (request,"index.html")

def registro(request):
	return render (request,"registro.html")
	
# Create your views here.
