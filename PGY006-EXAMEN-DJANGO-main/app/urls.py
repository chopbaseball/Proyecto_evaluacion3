from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('carrito/',carrito, name="carrito"),
    path('done/',delete_product, name="delete_product"),
    path('registro/',registroUsuario, name="registroUsuario"),
    path('suscripcion/',suscripcion, name="suscripcion"),
    path('apirandom/',apirandom, name="apirandom"),
    path('apiproducto/',apiproducto, name="apiproducto"),
    path('agregarproducto/',agregar_producto, name="agregar_producto"),
    path('agregarusuario/',agregar_usuario, name="agregar_usuario"),
    path('modificarProducto/<codigo>/',modificarProducto, name="modificarProducto"),
    path('modificarUsuario/<id>/',modificarUsuario, name="modificarUsuario"),
    path('eliminarProducto/<codigo>/',eliminarProducto, name="eliminarProducto"),
    path('eliminarUsuario/<id>/',eliminarUsuario, name="eliminarUsuario"),
    path('listarUsuarios/',listarUsuarios, name="listarUsuarios"),
    path('listarProductos/',listarProductos, name="listarProductos"),
    path('historial/',historialdecompras, name="historialdecompras"),
    path('listarSeguimiento/',listarSeguimiento, name="listarSeguimiento"),
    path('modificarSeguimiento/<id>/',modificarSeguimiento, name="modificarSeguimiento"),
]