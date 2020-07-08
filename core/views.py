from django.shortcuts import render, redirect
from .forms import ProveedorForm, InsumoForm
import requests

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def factura(request):

    return render(request, 'core/factura.html')   

def orden_compra(request):
    url_get_ordencompra = "http://ec2-100-25-239-160.compute-1.amazonaws.com:5000/get-id-orden-compra"
    results = requests.get(url_get_ordencompra).json()
    ordens = []
    for result in results:
        orden = []
        tipo.append(result["ID_orden_compra"])
        ordens.append(tipo)
    print (ordens)
    return render(request, 'core/orden_compra.html', {'ordens': ordens})
   

def crear_producto(request):
    url_get_tipoProducto = "http://54.146.107.251/tipo_producto"
    results = requests.get(url_get_tipoProducto).json()
    tipos = []
    for result in results:
        tipo = []
        tipo.append(result["ID_TIP_PROD"])
        tipo.append(result["TIPO_PROD"])
        tipos.append(tipo)
    print (tipos)
    return render(request, 'core/crear_producto.html', {'tipos': tipos})

def Agregar_proveedor(request):
    #proveedor = []
    #if request.method == "POST":
     #   RUT_PROV = request.POST["rut_prov"]
      #  NOM_COM = request.POST["NOM_COM"]
       # FONO = request.POST["FONO"]
       # EMAIL = request.POST["EMAIL"]
       # DIRECCION = request.POST["DIRECCION"]
       # ID_COMUNA = request.POST["ID_COMUNA"]
       # GIRO_COM = request.POST["GIRO_COM"]
       # RAZON_SOC = request.POST["RAZON_SOC"]
    #r = requests.post('http://54.146.107.251/proveedor').json()
    #return render(request, 'core/agregar_proveedor.html')   
    url_get_comuna = "http://54.146.107.251/comuna/"
    results = requests.get(url_get_comuna).json()
    comunas = []
    for result in results:
        comuna = []
        comuna.append(result["ID_COMUNA"])
        comuna.append(result["NOM_COMUNA"])
        comuna.append(result["ID_PROVINCIA"])
        comunas.append(comuna)
    print (comunas)
    return render(request, 'core/Agregar_proveedor.html', {'comunas': comunas})



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





def Agregar_insumos(request):
    url_get_tipoProducto = "http://54.146.107.251/tipo_producto"
    results = requests.get(url_get_tipoProducto).json()
    tipos = []
    for result in results:
        tipo = []
        tipo.append(result["ID_TIP_PROD"])
        tipo.append(result["TIPO_PROD"])
        tipos.append(tipo)
    print (tipos)
    return render(request, 'core/Agregar_insumos.html', {'tipos': tipos})



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
