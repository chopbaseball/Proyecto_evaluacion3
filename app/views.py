from itertools import product
import requests
from math import prod, trunc
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request,'app/index.html')


@login_required
def perro(request):
    #response = requests.get('url de nuestra api').json() #para api propia
    #response3 = requests.get('https://thronesapi.com/api/v2/Characters').json()

    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll,
        #'listaRM' : response3
    }

    historial = Historial.objects.all()
    e = 1
    for i in historial:
        e += 1

  

    if request.method == 'POST':
        codigo_producto = request.POST.get('codigo_producto')
        nombre_producto = request.POST.get('nombre_producto')
        precio_producto = request.POST.get('precio_producto')
        usuario = request.POST.get('user')

        if Carrito.objects.filter(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto)).exists():
            productoCarro = Carrito.objects.get(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto))
            productoCarro.cantidad += 1
            productoCarro.precio_producto += int(precio_producto)
            productoCarro.save()
        else:
            carrito = Carrito()
            carrito.cantidad = 1
            carrito.nombre_producto = request.POST.get('nombre_producto')
            carrito.precio_producto = request.POST.get('precio_producto')
            carrito.imagen_producto = request.POST.get('imagen_producto')
            carrito.codigo_producto = request.POST.get('codigo_producto')
            carrito.usuario = usuario
            carrito.save()

        if CarritoHist.objects.filter(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e)).exists():
            productoHist= CarritoHist.objects.get(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e))
            productoHist.cantidad_hist += 1
            productoHist.precio_hist += int(precio_producto)
            productoHist.save()
        else:
            historial = CarritoHist()
            historial.nombre_his = request.POST.get('nombre_producto')
            historial.precio_hist = request.POST.get('precio_producto')
            historial.imagen_hist = request.POST.get('imagen_producto')
            historial.codigo_his = request.POST.get('codigo_producto')
            historial.usuario_hist = usuario
            historial.oorden = e
           
            historial.cantidad_hist = 1
            historial.save()

        producto = Producto.objects.get(codigo = int(codigo_producto))
        producto.stock -= 1
        producto.save()

    return render(request,'app/perros.html', datos )

@login_required
def gato(request):
    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll
    }

    historial = Historial.objects.all()
    e = 1
    for i in historial:
        e += 1

  

    if request.method == 'POST':
        codigo_producto = request.POST.get('codigo_producto')
        nombre_producto = request.POST.get('nombre_producto')
        precio_producto = request.POST.get('precio_producto')
        usuario = request.POST.get('user')

        if Carrito.objects.filter(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto)).exists():
            productoCarro = Carrito.objects.get(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto))
            productoCarro.cantidad += 1
            productoCarro.precio_producto += int(precio_producto)
            productoCarro.save()
        else:
            carrito = Carrito()
            carrito.cantidad = 1
            carrito.nombre_producto = request.POST.get('nombre_producto')
            carrito.precio_producto = request.POST.get('precio_producto')
            carrito.imagen_producto = request.POST.get('imagen_producto')
            carrito.codigo_producto = request.POST.get('codigo_producto')
            carrito.usuario = usuario
            carrito.save()

        if CarritoHist.objects.filter(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e)).exists():
            productoHist= CarritoHist.objects.get(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e))
            productoHist.cantidad_hist += 1
            productoHist.precio_hist += int(precio_producto)
            productoHist.save()
        else:
            historial = CarritoHist()
            historial.nombre_his = request.POST.get('nombre_producto')
            historial.precio_hist = request.POST.get('precio_producto')
            historial.imagen_hist = request.POST.get('imagen_producto')
            historial.codigo_his = request.POST.get('codigo_producto')
            historial.usuario_hist = usuario
            historial.oorden = e
           
            historial.cantidad_hist = 1
            historial.save()

        producto = Producto.objects.get(codigo = int(codigo_producto))
        producto.stock -= 1
        producto.save()
        
    return render(request,'app/gatos.html',datos)

@login_required
def otros(request):
    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll
    }
    historial = Historial.objects.all()
    e = 1
    for i in historial:
        e += 1

  

    if request.method == 'POST':
        codigo_producto = request.POST.get('codigo_producto')
        nombre_producto = request.POST.get('nombre_producto')
        precio_producto = request.POST.get('precio_producto')
        usuario = request.POST.get('user')

        if Carrito.objects.filter(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto)).exists():
            productoCarro = Carrito.objects.get(Q(codigo_producto=codigo_producto) & Q(usuario= usuario) & Q(nombre_producto = nombre_producto))
            productoCarro.cantidad += 1
            productoCarro.precio_producto += int(precio_producto)
            productoCarro.save()
        else:
            carrito = Carrito()
            carrito.cantidad = 1
            carrito.nombre_producto = request.POST.get('nombre_producto')
            carrito.precio_producto = request.POST.get('precio_producto')
            carrito.imagen_producto = request.POST.get('imagen_producto')
            carrito.codigo_producto = request.POST.get('codigo_producto')
            carrito.usuario = usuario
            carrito.save()

        if CarritoHist.objects.filter(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e)).exists():
            productoHist= CarritoHist.objects.get(Q(codigo_his=codigo_producto) & Q(usuario_hist= usuario) & Q(nombre_his = nombre_producto) & Q(oorden=e))
            productoHist.cantidad_hist += 1
            productoHist.precio_hist += int(precio_producto)
            productoHist.save()
        else:

            historial = CarritoHist()
            historial.nombre_his = request.POST.get('nombre_producto')
            historial.precio_hist = request.POST.get('precio_producto')
            historial.imagen_hist = request.POST.get('imagen_producto')
            historial.codigo_his = request.POST.get('codigo_producto')
            historial.usuario_hist = usuario
            historial.oorden = e
           
            historial.cantidad_hist = 1
            historial.save()

        producto = Producto.objects.get(codigo = int(codigo_producto))
        producto.stock -= 1
        producto.save()
    return render(request,'app/otros.html',datos)

@login_required
def pago(request):
    
               

    return render(request,'app/pago.html')

@login_required
def carrito(request):
    carrito = Carrito.objects.all() #llama a todos los productos
    suscri = Suscripcion.objects.all()
    
    total = 0
    desc = 0
    totalFinal = 0
    codigo = 0
    

    historial = Historial.objects.all()
    code = 1
    for i in historial:
        code += 1
  
    
    for a in carrito :
        if request.user.get_username() in a.usuario:
            total += a.precio_producto
            desc += total * (5)/100
            totalFinal = total - desc

    if request.method == 'POST':
        for i in carrito:
            if request.user.get_username() == i.usuario:
                
                carritoeliminado = Carrito.objects.get(Q(codigo_producto=i.codigo_producto) & Q(usuario=i.usuario))
                
                hi = Historial()
                hi.precio = total
                hi.usuario = request.user.get_username()
                hi.orden = code
                hi.estado_id = 1
                hi.save()

                segui = Historial.objects.all()

                for x in segui :
                    codigo = codigo +1
                    se = Seguimiento()
                    se.codigoProducto = i.codigo_producto
                    se.nombre = i.nombre_producto
                    se.precio = x.precio
                    se.cantidad = i.cantidad
                    se.codigo = codigo
                    se.estado_id = 1
                    se.save()
                
                carritoeliminado.delete()
                
                return redirect(to="pago")
                

    datos = { #sirve para transportar los productos a la pagina
        'ListaCarrito' : carrito,
        
        'total' : total,
        'desc' : desc,
        'totalFinal' : totalFinal,
        'suscri' : suscri
    }

    return render(request,'app/carrito.html', datos)

@login_required
def eliminarProducto(request, codigo):
    carrito = Carrito.objects.get(codigo_producto=codigo)
    producto = Producto.objects.get(codigo = int(codigo))
    producto.stock += carrito.cantidad
    producto.save()
    
    his = CarritoHist.objects.all()
    for x in his:
        codigo = x.codigo_his
        usuario = x.usuario_hist



    CarritoHist.objects.filter(Q(codigo_his=codigo) & Q(usuario_hist=usuario)).delete()

    carrito.delete()
    return redirect(to="carrito")


def seguiCod(request):
    return render(request,'app/seguiCod.html')

def perfil(request):
    perfil = Historial.objects.all()
    carrito = CarritoHist.objects.all()

    datos = {
        'ListaHistorial' : perfil,
        'ListaCarrito' : carrito,
        
    }
    return render(request,'app/perfil.html',datos)

@permission_required('app.add_producto')
def agregarProducto(request): #seccion agregar
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')

    return render(request,'app/Productos/agregarProducto.html', datos)

@permission_required('app.view_producto')
def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    return render(request, 'app/Productos/listar.html', datos)

@permission_required('app.change_producto')
def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Modificado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/Productos/modificar.html', datos)

@permission_required('app.delete_producto')
def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar")

@permission_required('app.add_cliente')
def agregarCliente (request):

    datos = {
        'form' : ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Guardado Correctamente!')

    return render(request, 'app/cliente/agregarCliente.html',datos)

@permission_required('app.view_cliente')
def listarCliente (request):

    productosAll = Cliente.objects.all()
    datos = {
        'listarCliente' : productosAll
    }
    
    return render(request,'app/cliente/listarCliente.html',datos)

@permission_required('app.change_cliente')
def modificarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    datos = {
        'form' : ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Modificado correctamente!')
            datos['form'] = formulario
    return render(request, 'app/cliente/modificarCliente.html', datos)

@permission_required('app.delete_cliente')
def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect(to="listarCliente")

def login(request):
    return render(request,'registration/login.html')

def registro(request):
    datos={
        'form' : FormularioUserResgistro()
    }
    if request.method == 'POST':
        formulario = FormularioUserResgistro(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='Cliente')    
            group.user_set.add(user)
            suscrito = Suscripcion()
            suscrito.user = request.POST.get('username')
            suscrito.estado = 0
            suscrito.save()
            messages.success(request,'Usuario Registrado Correctamente!')
    return render(request,'registration/registro.html',datos)

@login_required
def suscripcion(request):
    psuscripcionesAll = Suscripcion.objects.all()

    datos = {
        'suscrip' : psuscripcionesAll
    }

    if request.method == 'POST':
        sus = Suscripcion()
        sus.user = request.POST.get('user')
        sus.estado = request.POST.get('estado')
        sus.save()

    return render(request,'app/suscripcion.html',datos)

@login_required
def apiExterna(request):
    apiExterna = requests.get('https://thronesapi.com/api/v2/Characters').json()

    datos = {
        'ApiExterna' : apiExterna
    }
    return render(request,'app/externas/apiexterna.html',datos)


@login_required
def seguimiento(request):
    datosALL = Seguimiento.objects.all()
    datos = {
        'datos' : datosALL

    }
    return render(request,'app/seguimiento.html',datos)



@login_required
def cambiarEstado(request):

    datosALL = Seguimiento.objects.all()
    datos = {
        'datos' : datosALL
    }
    return render(request,'app/cambiarEstado.html',datos)



def modificarEstado(request, codigo):
    
    seguimiento = Seguimiento.objects.get(codigo=codigo)
    datos = {
        'form' : SeguimientoForm(instance=seguimiento)
    }
    if request.method == 'POST':
        formulario = SeguimientoForm(request.POST, files=request.FILES, instance=seguimiento)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Estado Modificado correctamente!')
            datos['form'] = formulario
    return render(request, 'app/modificarEstado.html', datos)




@login_required
def apiNuestra(request):
    apiNuestra = requests.get('https://amorquiltro-default-rtdb.firebaseio.com/AmorDeQuiltro.json').json()

    datos = {
        'apiNuestra' : apiNuestra
    }
    return render(request,'app/api/apiNuestra.html',datos)

