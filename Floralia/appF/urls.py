from django.urls import path
from appF import views

urlpatterns = [
    path('inicio/', views.inicio, name='Inicio'),
    path('registro/',views.registro, name='registro'),
]