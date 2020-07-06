from django.shortcuts import render, redirect

from .forms import ProveedorForm, InsumoForm
import requests

# Create your views here.

def index(request):

    return render(request, 'core/index.html')




def Agregar_proveedor(request):
    data = {
        'form':ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Proveedor agregado correctamente"

    return render(request, 'core/Agregar_proveedor.html',data)     


def Agregar_insumos(request):
    data = {
        'form':InsumoForm()
    }

    if request.method == 'POST':
        formulario = InsumoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Insumo agregado correctamente"

    return render(request, 'core/Agregar_insumos.html',data)     




def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    
    return redirect(to="listar_proveedor")



def Eliminar_insumos(request, id):
    insumo = Insumo.objects.get(id=id)
    insumo.delete()
    
    return redirect(to="listar_insumos")        
    



def Modificar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid(): 
            formulario.save()
            data['mensaje'] = "Proveedor modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/Modificar_proveedor.html', data)        



def Listar_proveedor(request):
    url_get_proveedor = "http://54.146.107.251/proveedor"
    results = requests.get(url_get_proveedor).json()
    proveedores = []
    for result in results:
        proveedor = []
        proveedor.append(result["RUT_PROV"])
        proveedor.append(result["NOM_COM"])
        proveedor.append(result["FONO"])
        proveedor.append(result["EMAIL"])
        proveedor.append(result["DIRECCION"])
        proveedor.append(result["ID_COMUNA"])
        proveedor.append(result["GIRO_COM"])
        proveedor.append(result["RAZON_SOC"])

        proveedores.append(proveedor)
    print (proveedores)
    return render(request, 'core/Listar_proveedor.html', {'proveedores': proveedores})

def Listar_insumos(request):
    url_get_insumos = "http://54.146.107.251/producto"
    results = requests.get(url_get_insumos).json()
    productos = []
    for result in results:
        producto = []
        producto.append(result["ID_PROD"])

        producto.append(result["ID_TIP_PROD"])

        producto.append(result["NOM_PROD"])
        producto.append(result["MARCA"])
        producto.append(result["MODELO"])
        producto.append(result["DESCRIPCION"])
        producto.append(result["PRECIO"])
        producto.append(result["IMAGEN_0"])

        producto.append(result["STOCK"])
        productos.append(producto)
    print (productos)
    return render(request, 'core/Listar_insumos.html', {'productos': productos})



def Modificar_insumos(request, id):
    insumo = Insumo.objects.get(id=id)
    data = {
        'form': InsumoForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, instance=insumo)
        if formulario.is_valid(): 
            formulario.save()
            data['mensaje'] = "Insumo modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/Modificar_insumos.html', data)            
