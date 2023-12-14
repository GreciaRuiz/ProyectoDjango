from django.contrib import admin
from .models import Proveedor, Usuario

class ProveedorAdmin(admin.ModelAdmin):
	list_display=('nombre','telefono','mail','direccion')
	search_fields=('nombre','direccion')

class UsuarioAdmin(admin.ModelAdmin):
	list_display=('email', 'nombre', 'apellido', 'password')


admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Usuario, UsuarioAdmin)
# Register your models here.
