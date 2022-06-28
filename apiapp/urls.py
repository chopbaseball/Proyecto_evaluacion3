

from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import URLPattern
from rest_framework import routers
from .views import *


#agregar una ruta en la api
router = routers.DefaultRouter()
router.register (r'Productos',ProductoViewSet)
router.register (r'TipoProducto',TipoProductoViewSet)
router.register (r'Comuna', ComunaViewSet)
router.register (r'Cliente',ClienteViewSet)

URLPattern =[
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]