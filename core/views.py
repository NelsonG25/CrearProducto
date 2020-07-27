from django.shortcuts import render, redirect
from .forms import ProveedorForm, InsumoForm
from .login import lambda_handler
import requests
import http.client

def index(request):
    headers = request.session['Headers']
    username = request.session['Username']
    print(headers)
    return render(request, 'core/index.html', {'username': username})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena') 

        json_data = lambda_handler(username,password)
        print(json_data)
        if json_data['success'] == True:
            token = json_data['data']['access_token']
            headers = {
                'content-type': "application/json",
                'authorization': "Bearer " + token
            }
            request.session['Headers'] = headers
            request.session['Username'] = username

            return redirect('index')
        else:
            return render(request, 'core/login.html')
    return render(request, 'core/login.html')


def factura(request):
    headers = request.session['Headers']
    url = "https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/get-id-compra"
    operacion = requests.get(url, headers=headers).json()
    nOperacion = operacion.get("idOperacion")
    codArea = 201 
    departamento = "creacion de productos" 

    if request.method == 'POST':
        nroOperacion = nOperacion
        nroFactura = request.POST.get('nroFac')
        rutProveedor = request.POST.get('rutProv')
        fecha = request.POST.get('fecha')
        totalNeto = request.POST.get('totalNeto')
        codTrabajador = codArea
        idDepartamento = departamento
        nroOrdenCompra = request.POST.get('nroOrden')
        detalleOrdenCompra = [
            {"idProducto": request.POST.get('insumo1'),"cantidad": request.POST.get('cantidad1')},
            {"idProducto": request.POST.get('insumo2'),"cantidad": request.POST.get('cantidad2')},
            {"idProducto": request.POST.get('insumo3'),"cantidad": request.POST.get('cantidad3')},
            {"idProducto": request.POST.get('insumo4'),"cantidad": request.POST.get('cantidad4')},
        ]

        url = 'https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/agregar-compra' 
        response = requests.post(url, json={"nroOperacion": nroOperacion, "nroFactura": nroFactura, 'rutProveedor': rutProveedor, 'fecha': fecha, 'totalNeto': totalNeto, 'codTrabajador': codTrabajador, "idDepartamento": idDepartamento, "nroOrdenCompra": nroOrdenCompra, 'detalleOrdenCompra': detalleOrdenCompra},headers=headers)

    return render(request, 'core/factura.html')   


def orden_compra(request): 
    headers = request.session['Headers']
    url = "https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/get-id-orden-compra"
    orden = requests.get(url, headers=headers).json()
    nOrden = orden.get("idOrdenCompra")
    codArea = 301 
    print(nOrden)
    if request.method == 'POST':
        nroOrdenCompra = nOrden
        rutProveedor = request.POST.get('rutProv')
        fecha = request.POST.get('fecha')
        totalNeto = request.POST.get('totalNeto')
        codTrabajador = codArea
        detalleOrdenCompra = [
            {"idProducto": request.POST.get('insumo1'), "cantidad": request.POST.get('cantidad1')},
            {"idProducto": request.POST.get('insumo2'), "cantidad": request.POST.get('cantidad2')},
            {"idProducto": request.POST.get('insumo3'), "cantidad": request.POST.get('cantidad3')},
            {"idProducto": request.POST.get('insumo4'), "cantidad": request.POST.get('cantidad4')},
        ]

        url = 'https://oawjeg21mb.execute-api.us-east-1.amazonaws.com/contabilidad/agregar-orden-compra' 
        response = requests.post(url, json={"nroOrdenCompra": nroOrdenCompra, 'rutProveedor': rutProveedor, 'fecha': fecha, 'totalNeto': totalNeto, 'codTrabajador': codTrabajador, 'detalleOrdenCompra': detalleOrdenCompra},headers=headers)
    
    return render(request, 'core/orden_compra.html', {'orden': orden})


def crear_producto(request):
    headers = request.session['Headers']
    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/tipo-producto"
    tipo = requests.get(url, headers=headers).json()
    tipos = []
    for data in tipo:
        tipo = []
        tipo.append(data['ID_TIP_PROD'])
        tipo.append(data['TIPO_PROD'])
        tipos.append(tipo)

    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/estado"
    estado = requests.get(url, headers=headers).json()
    estados = []
    for data in estado:
        estado = []
        estado.append(data['ID_ESTADO'])
        estado.append(data['NOM_ESTADO'])
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
        IMAGEN_0 = request.POST.get('imagen0')
        IMAGEN_1 = request.POST.get('imagen1')
        IMAGEN_2 = request.POST.get('imagen2')
        IMAGEN_3 = request.POST.get('imagen3')
        IMAGEN_4 = request.POST.get('imagen4')
        
        url = 'https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/producto'
        response = requests.post(url, json={'ID_PROD': ID_PROD, 'ID_ESTADO': ID_ESTADO, 'ID_TIP_PROD': ID_TIP_PROD, 'RUT_PROV': RUT_PROV, 'NOM_PROD': NOM_PROD, 'MARCA': MARCA, 'MODELO': MODELO, 'DESCRIPCION': DESCRIPCION, 'PRECIO': PRECIO}, headers=headers)

    return render(request, 'core/crear_producto.html',{'tipos': tipos,'estados': estados})


def Agregar_proveedor(request):
    headers = request.session['Headers']
    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/comuna"
    comuna = requests.get(url, headers=headers).json()
    comunas = []
    for data in comuna:
        comuna = []
        comuna.append(data['ID_COMUNA'])
        comuna.append(data['NOM_COMUNA'])
        comunas.append(comuna)

    if request.method == 'POST':
        RUT_PROV = request.POST.get('rutProv')
        NOM_COM = request.POST.get('nomCom')
        FONO = request.POST.get('fono')
        EMAIL = request.POST.get('email')
        DIRECCION = request.POST.get('direc')
        ID_COMUNA = request.POST.get('comuna')
        GIRO_COM = request.POST.get('giroCom')
        RAZON_SOC = request.POST.get('razonSoc')
        url = 'https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/proveedor'
        response = requests.post(url, json={'RUT_PROV' :RUT_PROV, 'NOM_COM' :NOM_COM , 'FONO': FONO, 'EMAIL': EMAIL, 'DIRECCION': DIRECCION, 'ID_COMUNA': ID_COMUNA, 'GIRO_COM': GIRO_COM, 'RAZON_SOC': RAZON_SOC}, headers=headers)

    return render(request, 'core/Agregar_proveedor.html', {'comunas': comunas})


def Agregar_insumos(request):
    headers = request.session['Headers']
    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/tipo-producto"
    tipo = requests.get(url, headers=headers).json()
    tipos = []
    for data in tipo:
        tipo = []
        tipo.append(data['ID_TIP_PROD'])
        tipo.append(data['TIPO_PROD'])
        tipos.append(tipo)

    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/estado"
    estado = requests.get(url, headers=headers).json()
    estados = []
    for data in estado:
        estado = []
        estado.append(data['ID_ESTADO'])
        estado.append(data['NOM_ESTADO'])
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
        IMAGEN_0 = request.POST.get('imagen0')
        IMAGEN_1 = request.POST.get('imagen1')
        IMAGEN_2 = request.POST.get('imagen2')
        IMAGEN_3 = request.POST.get('imagen3')
        IMAGEN_4 = request.POST.get('imagen4')
        
        url = 'https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/producto'
        response = requests.post(url, json={'ID_PROD': ID_PROD, 'ID_ESTADO': ID_ESTADO, 'ID_TIP_PROD': ID_TIP_PROD, 'RUT_PROV': RUT_PROV, 'NOM_PROD': NOM_PROD, 'MARCA': MARCA, 'MODELO': MODELO, 'DESCRIPCION': DESCRIPCION, 'PRECIO': PRECIO},headers=headers)

    return render(request, 'core/Agregar_insumos.html',{'tipos': tipos,'estados': estados})


def Listar_proveedor(request):
    headers = request.session['Headers']
    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/comuna"
    comuna = requests.get(url, headers=headers).json()
    comunas = []
    for data in comuna:
        comuna = []
        comuna.append(data['ID_COMUNA'])
        comuna.append(data['NOM_COMUNA'])
        comunas.append(comuna)

    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/proveedor"
    proveedor = requests.get(url, headers=headers).json()
    proveedores = []
    for data in proveedor:
        proveedor = []
        proveedor.append(data["RUT_PROV"])
        proveedor.append(data["NOM_COM"])
        proveedor.append(data["FONO"])
        proveedor.append(data["EMAIL"])
        proveedor.append(data["DIRECCION"])
        proveedor.append(data["ID_COMUNA"])
        proveedor.append(data["GIRO_COM"])
        proveedor.append(data["RAZON_SOC"])
        proveedores.append(proveedor)

    return render(request, 'core/Listar_proveedor.html', {'proveedores': proveedores, 'comunas': comunas})


def Listar_insumos(request):
    headers = request.session['Headers']
    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/tipo-producto"
    tipo = requests.get(url, headers=headers).json()
    tipos = []
    for data in tipo:
        tipo = []
        tipo.append(data["ID_TIP_PROD"])
        tipo.append(data["TIPO_PROD"])
        tipos.append(tipo)

    url = "https://tonwzkx6o5.execute-api.us-east-1.amazonaws.com/stock/producto"
    producto = requests.get(url, headers=headers).json()
    productos = []
    for data in producto:
        producto = []
        producto.append(data["ID_PROD"])
        producto.append(data["ID_TIP_PROD"])
        producto.append(data["NOM_PROD"])
        producto.append(data["MARCA"])
        producto.append(data["MODELO"])
        producto.append(data["DESCRIPCION"])
        producto.append(data["PRECIO"])
        producto.append(data["IMAGEN_0"])
        producto.append(data["STOCK"])
        productos.append(producto)

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

