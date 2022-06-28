from itertools import product
from math import prod, trunc
from pprint import pprint
import requests
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q
# Create your views here.


### Todos los index ###


def index(request):
    productosAll = Producto.objects.all()

    datos = {
        'listaProductos' : productosAll
    }

    #Carrito Historico
    historial = Historial.objects.all()
    code = 1
    for i in historial:
        code += 1

    if request.method == 'POST':
        prod = Carrito()
        codigoprod = request.POST.get('txtCodigo')
        stock = request.POST.get('txtStock')
        precio = request.POST.get('txtPrecio')
        usuarioprod = request.POST.get('txtUsuario')
        nombre = request.POST.get('txtNombre')

        if Carrito.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre)).exists():
            product = Carrito.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            prod.nombre = request.POST.get('txtNombre')
            prod.codigo = request.POST.get('txtCodigo')
            prod.usuario = request.POST.get('txtUsuario')
            prod.cantidad = request.POST.get('txtStock')
            prod.imagen = request.POST.get('txtImagen')
            prod.precio = int(stock) * int(precio)
            prod.save()

        if CarritoHistorico.objects.filter(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre) & Q(codigoorden=code)).exists():
            product = CarritoHistorico.objects.get(Q(codigo=codigoprod) & Q(usuario=usuarioprod) & Q(nombre=nombre) & Q(codigoorden=code))
            product.cantidad += int(stock)
            product.precio += int(stock) * int(precio)
            product.save()
        else:
            carroHist = CarritoHistorico()
            carroHist.nombre = request.POST.get('txtNombre')
            carroHist.codigo = request.POST.get('txtCodigo')
            carroHist.codigoorden = code
            carroHist.usuario = request.user.get_username()
            carroHist.precio = int(stock) * int(precio)
            carroHist.cantidad = request.POST.get('txtStock')
            carroHist.imagen = request.POST.get('txtImagen')
            carroHist.save()

        stock = request.POST.get('txtStock')
        codigo = request.POST.get('txtCodigo')
        product = Producto.objects.get(codigo=int(codigo))
        product.stock -= int(stock)
        product.save()

    return render(request, 'app/index.html', datos)

@login_required
def delete_product(request):
    historial = Historial.objects.all()
    code = 1
    for i in historial:
        code += 1

    carritoAll = Carrito.objects.all()
    total = 0
    totalDesc = 0
    for i in carritoAll:
        if request.user.get_username() in i.usuario:
            total += i.precio
            totalDesc += ( i.precio) * 0.95

    if request.method == "GET":
        #Creo una orden
        hist = Historial()
        hist.orden = code
        hist.usuario = request.user.get_username()
        hist.preciototal = total
        hist.estado = Seguimiento.objects.get(codigo=1)
        hist.save()
        for i in carritoAll:
            if request.user.get_username() == i.usuario:
                item = Carrito.objects.get(Q(codigo=i.codigo) & Q(usuario=i.usuario))
                item.delete()
    return render(request, "app/compra-finalizada.html")

@login_required
def carrito(request):
    carritoAll = Carrito.objects.all()
    usuario = Suscrito.objects.all()
    total = 0
    totalDesc = 0
    desc = 0
    for i in carritoAll:
        if request.user.get_username() in i.usuario:
            total += i.precio
            totalDesc += ( i.precio) * 0.95
            desc = total - totalDesc
            
    datos = {
        'listarCarrito' : carritoAll,
        'total' : total,
        'totalDesc' : totalDesc,
        'usuario' : usuario,
        'desc' : desc
    }
    if request.method == "POST":
        prod = Carrito()
        prod.id = request.POST.get('id')
        borrado = prod.delete()

        codigo = request.POST.get('txtCodigo')
        usuario = request.POST.get('txtUsuario')

        if borrado[0] == 0:
            stock = request.POST.get('txtStock')
            codigo = request.POST.get('txtCodigo')
            product = Producto.objects.get(codigo=int(codigo))
            product.stock += int(stock)
            product.save()
            CarritoHistorico.objects.filter(Q(codigo=codigo) & Q(usuario=usuario)).delete()
    return render(request,'app/carrito.html',datos)

@login_required
def historialdecompras(request):
    historial = Historial.objects.all()
    carrito = CarritoHistorico.objects.all()
    datos ={
        'listaHistorial' : historial,
        'listaCarrito' : carrito,
    }
    return render(request, 'app/historial.html', datos)

@login_required
def suscripcion(request):
    usuario = Suscrito.objects.all()
    datos ={
        'usuario' : usuario,
    }
    if request.method == 'POST':
        usuarios = Suscrito()
        usuarios.nombre = request.POST.get('username')
        usuarios.estado = request.POST.get('boolean')
        usuarios.save()
    return render(request, 'app/suscripcion.html', datos)


def registroUsuario(request):
    datos = {
        'form' : FormularioUserRegistro
    }
    if request.method == 'POST':
        formulario = FormularioUserRegistro(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='cliente')    
            group.user_set.add(user)
            suscrito = Suscrito()
            suscrito.nombre = request.POST.get('username')
            suscrito.estado = "No"
            suscrito.save()
            messages.success(request,'Usuario Registrado correctamente!')
    return render(request,'registration/registroUsuario.html',datos)

@login_required
def apirandom(request):
    response = requests.get('https://dbd-api.herokuapp.com/perks').json()
    datos ={
        'listaDbd' : response
    }
    return render(request,'app/apirandom.html', datos)

@login_required
def apiproducto(request):
    response = requests.get('http://127.0.0.1:8000/api/Producto/').json()
    datos ={
        'listaProductos' : response
    }
    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('txtNombre')
        prod.usuario = request.POST.get('txtUsuario')
        prod.precio = request.POST.get('txtPrecio')
        prod.imagen = request.POST.get('txtImagen')
        prod.cantidad = request.POST.get('txtStock')
        prod.save()
    return render(request,'app/apiproducto.html', datos)

@permission_required('app.add_producto')
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
    return render(request,'app/productos/agregar_producto.html', datos)

@permission_required('app.add_usuario')
def agregar_usuario(request):
    datos = {
        'form' : UserForm()
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario creado correctamente!"
    return render(request,'app/usuarios/agregar_usuario.html', datos)

@permission_required('app.change_producto')
def modificarProducto(request, codigo):
    productos =  Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES, instance=productos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            datos['form'] = formulario
    return render(request,'app/productos/modificarProducto.html', datos)    

def modificarUsuario(request, id):
    usuario =  User.objects.get(id=id)
    datos = {
        'form' : UserForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario modificado correctamente!"
            datos['form'] = formulario
    return render(request,'app/usuarios/modificarUsuario.html', datos) 

@permission_required('app.add_producto')
def listarProductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    return render(request,'app/productos/listarProductos.html',datos)

@permission_required('app.add_usuario')
def listarUsuarios(request):
    usuariosAll = User.objects.all()
    datos = {
        'listarUsuarios' : usuariosAll
    }
    return render(request,'app/usuarios/listarUsuarios.html',datos)

def listarSeguimiento(request):
    historialAll = Historial.objects.all()
    datos = {
        'listarHistorial' : historialAll
    }
    return render(request,'app/seguimiento/listarSeguimiento.html', datos)

def modificarSeguimiento(request, id):
    seg =  Historial.objects.get(id=id)
    datos = {
        'form' : HistorialForm(instance=seg)
    }
    if request.method == 'POST':
        formulario = HistorialForm(request.POST, files=request.FILES, instance=seg)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Seguimiento guardado correctamente!')
            datos['form'] = formulario
    return render(request,'app/seguimiento/modificarSeguimiento.html', datos) 

@permission_required('app.delete_usuario')
def eliminarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect(to="listarUsuarios")

@permission_required('app.delete_producto')
def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to="listarProductos")