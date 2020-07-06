from django import forms
from django.forms import ModelForm
from .models import Proveedor, Insumo

class ProveedorForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)

    class Meta:
        model = Proveedor
        fields = ['nombre', 'rut', 'correo', 'region', 'comuna', 'direccion' ]


class InsumoForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)

    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre_Insumo', 'descripcion', 'valor', 'marca', 'modelo' ]        