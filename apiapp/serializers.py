from pyexpat import model

from attr import field
from rest_framework import serializers
from app.models import *

class ProductoSerializer (serializers.Modelserializers):
    class Meta:
        model = Producto
        field = '__all__'

class TipoProductoSerializer (serializers.Modelserializers):
    class Meta:
        model = TipoProducto
        field = '__all__'  

class ComunaSerializer (serializers.Modelserializers):
    class Meta:
        model = Comuna
        field = '__all__'  

class Cliente (serializers.Modelserializers):
    class Meta:
        model = Cliente
        field = '__all__'  