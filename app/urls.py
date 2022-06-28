from importlib.resources import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('perros/', perro, name="perro"),
    path('gatos/', gato, name="gato"),
    path('otros/', otros, name="otro"),
    path('pago/', pago, name="pago"),
    path('carrito/', carrito, name="carrito"),
    
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('seguiCod/', seguiCod, name="seguiCod"),
    path('perfil/', perfil, name="perfil"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('modificar/<codigo>', modificar, name="modificar"),
    path('listar/', listar, name="listar"),
    path('eliminar/<codigo>', eliminar, name="eliminar"),
    path('agregarCliente/', agregarCliente, name="agregarCliente"),
    path('listarCliente/',listarCliente,name="listarCliente"),
    path('modificarCliente/<codigo>', modificarCliente, name="modificarCliente"),
    path('eliminarCliente/<codigo>', eliminarCliente, name="eliminarCliente"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('eliminarProducto/<codigo>', eliminarProducto, name="eliminarProducto"),
    path('cambiarEstado/', cambiarEstado, name="cambiarEstado"),
    path('modificarEstado/<codigo>', modificarEstado, name="modificarEstado"),
    #path('apis/', apis, name="apis"),
    path('apiExterna/', apiExterna, name="apiExterna"),
    path('apiNuestra/', apiNuestra, name="apiNuestra"),
]


