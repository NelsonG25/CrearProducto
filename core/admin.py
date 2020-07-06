from django.contrib import admin
from .models import Proveedor, Insumo
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'correo', 'direccion', 'region' ]
    search_fields = ['nombre', 'rut']
    list_filter = ['region']
    list_per_page = 15


admin.site.register(Proveedor,ProveedorAdmin)



class InsumoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre_Insumo', 'valor', 'marca', 'modelo' ]
    search_fields = ['codigo', 'nombre_Insumo']
    list_filter = ['marca']
    list_per_page = 15


admin.site.register(Insumo,InsumoAdmin)

