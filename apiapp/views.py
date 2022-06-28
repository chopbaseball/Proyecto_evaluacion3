from multiprocessing.connection import Client
from django.shortcuts import render
#from matplotlib.pyplot import cla
#from numpy import product
from rest_framework import viewsets
from app.models import *
from .serializers import *
# Create your views here.

class ProductoViewSet (viewsets.ModelviewSet):
    queryset = Producto.objects.all()
    serializers_class = ProductoSerializer

class TipoProductoViewSet (viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializers_class = TipoProductoSerializer

class ComunaViewSet (viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializers_class = ComunaSerializer

class ClienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializers_class = Cliente
