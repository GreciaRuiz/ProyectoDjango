from django.urls import path
from appF import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('registro/',views.registro, name='registro'),
    path('login/',views.login, name='login'),
    path('plantas/',views.plantas, name='plantas'),
    path('macetas/',views.macetas, name='macetas')
]