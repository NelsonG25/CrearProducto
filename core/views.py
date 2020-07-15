from django.shortcuts import render, redirect
from .forms import ProveedorForm, InsumoForm
import requests

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def login(request):

    return render(request, 'core/login.html')

def factura(request):
    if request.method == 'POST':
        nroOperacion = request.POST.get('nroOper')
        nroFactura = request.POST.get('nroFac')
        rutProveedor = request.POST.get('rutProv')
        fecha = request.POST.get('fecha')
        totalNeto = request.POST.get('totalNeto')
        codTrabajador = request.POST.get('codTrab')
        idDepartamento = request.POST.get('idDep')
        nroOrdenCompra = request.POST.get('nroOrden')
        detalleCompra = request.POST.get('detCom')

        url = 'https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/agregar-orden-compra'
    #    #headers = {token}
        response = requests.post(url, json={'nroOperacion': nroOperacion, 'nroFactura': nroFactura, 'rutProveedor': rutProveedor, 'fecha': fecha, 'totalNeto': totalNeto, 'codTrabajador': codTrabajador, 'idDepartamento': idDepartamento, 'nroOrdenCompra': nroOrdenCompra, 'detalleCompra': detalleCompra})
    #     #json_data = registro_insumo(ID_PROD,ID_ESTADO,ID_TIP_PROD,RUT_PROV,NOM_PROD,MARCA,MODELO,DESCRIPCION,PRECIO,PRECIO_V,IMAGEN_0,STOCK)
        print(response)
    return render(request, 'core/factura.html')   

def orden_compra(request):
    url_get_ordencompra = "https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/get-id-orden-compra"
    results = requests.get(url_get_ordencompra).json()
    ordens = []
    for result in results:
        orden = []
        tipo.append(result["ID_orden_compra"])
        ordens.append(tipo)
    print (ordens)
    return render(request, 'core/orden_compra.html', {'ordens': ordens})
   

def crear_producto(request):
    if request.method == 'POST':
        ID_PROD = request.POST.get('idProd')
        ID_ESTADO = request.POST.get('id_estado')
        ID_TIP_PROD = request.POST.get('id_tip_prod')
        RUT_PROV = request.POST.get('rutProv')
        NOM_PROD = request.POST.get('nomInsumo')
        MARCA = request.POST.get('marca')
        MODELO = request.POST.get('modelo')
        DESCRIPCION = request.POST.get('descrip')
        PRECIO = request.POST.get('valor')
        PRECIO_V = request.POST.get('valorVenta')
        IMAGEN_0 = request.POST.get('imagen0')
        IMAGEN_1 = request.POST.get('imagen1')
        IMAGEN_2 = request.POST.get('imagen2')
        IMAGEN_3 = request.POST.get('imagen3')
        IMAGEN_4 = request.POST.get('imagen4')
        STOCK = request.POST.get('stock')
        url = 'http://54.146.107.251/producto'
       #headers = {token}
        response = requests.post(url, json={'ID_PROD': ID_PROD, 'ID_ESTADO': ID_ESTADO, 'ID_TIP_PROD': ID_TIP_PROD, 'RUT_PROV': RUT_PROV, 'NOM_PROD': NOM_PROD, 'MARCA': MARCA, 'MODELO': MODELO, 'DESCRIPCION': DESCRIPCION, 'PRECIO': PRECIO, 'PRECIO_V': PRECIO_V, 'IMAGEN_0': IMAGEN_0, 'IMAGEN_1': IMAGEN_1, 'IMAGEN_2': IMAGEN_2, 'IMAGEN_3': IMAGEN_3, 'IMAGEN_4': IMAGEN_4, 'STOCK': STOCK})
        #json_data = registro_insumo(ID_PROD,ID_ESTADO,ID_TIP_PROD,RUT_PROV,NOM_PROD,MARCA,MODELO,DESCRIPCION,PRECIO,PRECIO_V,IMAGEN_0,STOCK)
        print(response)
    return render(request, 'core/Agregar_insumos.html')

def Agregar_proveedor(request,*args):
    url_get_insumos = "http://54.146.107.251/comuna/"
    results = requests.get(url_get_insumos).json()
    comunas = []
    for result in results:
        comuna = []
        comuna.append(result["ID_COMUNA"])
        comuna.append(result["NOM_COMUNA"])
        comunas.append(comuna)

    if request.method == 'POST':
        #registro_prov = {}
        RUT_PROV = request.POST.get('rutProv')
        NOM_COM = request.POST.get('nomCom')
        FONO = request.POST.get('fono')
        EMAIL = request.POST.get('email')
        DIRECCION = request.POST.get('direc')
        ID_COMUNA = request.POST.get('comuna')
        GIRO_COM = request.POST.get('giroCom')
        RAZON_SOC = request.POST.get('razonSoc')
        url = 'http://54.146.107.251/proveedor'
       #headers = {token}
        response = requests.post(url, json={'RUT_PROV' :RUT_PROV, 'NOM_COM' :NOM_COM , 'FONO': FONO, 'EMAIL': EMAIL, 'DIRECCION': DIRECCION, 'ID_COMUNA': ID_COMUNA, 'GIRO_COM': GIRO_COM, 'RAZON_SOC': RAZON_SOC})
        #json_data = registro_prov(RUT_PROV,NOM_COM,FONO,EMAIL,DIRECCION,ID_COMUNA,GIRO_COM,RAZON_SOC)
        print(response)
        if response.status_code == 201:
            print("Proveedor Agregado correctamente")
    return render(request, 'core/Agregar_proveedor.html', {'comunas': comunas})


def Agregar_insumos(request,*args):
    url_get_insumos = "http://54.146.107.251/tipo_producto/"
    results = requests.get(url_get_insumos).json()
    tipos = []
    for result in results:
        tipo = []
        tipo.append(result["ID_TIP_PROD"])
        tipo.append(result["TIPO_PROD"])
        tipos.append(tipo)

    url_get_estados = "http://54.146.107.251/estado/"
    results = requests.get(url_get_estados).json()
    estados = []
    for result in results:
        estado = []
        estado.append(result["ID_ESTADO"])
        estado.append(result["NOM_ESTADO"])
        estados.append(estado)

    if request.method == 'POST':
        ID_PROD = request.POST.get('idProd')
        ID_ESTADO = request.POST.get('id_estado')
        ID_TIP_PROD = request.POST.get('id_tip_prod')
        RUT_PROV = request.POST.get('rutProv')
        NOM_PROD = request.POST.get('nomInsumo')
        MARCA = request.POST.get('marca')
        MODELO = request.POST.get('modelo')
        DESCRIPCION = request.POST.get('descrip')
        PRECIO = request.POST.get('valor')
        PRECIO_V = request.POST.get('valorVenta')
        IMAGEN_0 = request.POST.get('imagen0')
        IMAGEN_1 = request.POST.get('imagen1')
        IMAGEN_2 = request.POST.get('imagen2')
        IMAGEN_3 = request.POST.get('imagen3')
        IMAGEN_4 = request.POST.get('imagen4')
        STOCK = request.POST.get('stock')
        url = 'http://54.146.107.251/producto'
       #headers = {token}
        response = requests.post(url, json={'ID_PROD': ID_PROD, 'ID_ESTADO': ID_ESTADO, 'ID_TIP_PROD': ID_TIP_PROD, 'RUT_PROV': RUT_PROV, 'NOM_PROD': NOM_PROD, 'MARCA': MARCA, 'MODELO': MODELO, 'DESCRIPCION': DESCRIPCION, 'PRECIO': PRECIO, 'PRECIO_V': PRECIO_V, 'STOCK': STOCK})
        #json_data = registro_insumo(ID_PROD,ID_ESTADO,ID_TIP_PROD,RUT_PROV,NOM_PROD,MARCA,MODELO,DESCRIPCION,PRECIO,PRECIO_V,IMAGEN_0,STOCK)
        print(response)
    return render(request, 'core/Agregar_insumos.html',{'tipos': tipos,'estados': estados})


def Listar_proveedor(request):
    url_get_comunas = "http://54.146.107.251/comuna/"
    results = requests.get(url_get_comunas).json()
    comunas = []
    for result in results:
        comuna = []
        comuna.append(result["ID_COMUNA"])
        comuna.append(result["NOM_COMUNA"])
        comunas.append(comuna)

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
    return render(request, 'core/Listar_proveedor.html', {'proveedores': proveedores, 'comunas': comunas})

def Listar_insumos(request):
    url_get_insumos = "http://54.146.107.251/tipo_producto/"
    results = requests.get(url_get_insumos).json()
    tipos = []
    for result in results:
        tipo = []
        tipo.append(result["ID_TIP_PROD"])
        tipo.append(result["TIPO_PROD"])
        tipos.append(tipo)


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
    return render(request, 'core/Listar_insumos.html', {'productos': productos, 'tipos': tipos})


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
