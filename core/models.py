from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=80)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=60)
    region = models.CharField(max_length=50)  
    comuna = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.rut



class Insumo(models.Model):

    codigo =models.CharField(max_length=10)
    nombre_Insumo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    valor = models.IntegerField()
    marca = models.CharField(max_length=50)  
    modelo = models.CharField(max_length=50)

    

    def __str__(self):
        return self.codigo
    

