from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'Producto', ProductoViewSet)
router.register(r'TipoProducto', TipoProductoViewSet)
router.register(r'Usuario', UserViewSet)
router.register(r'TipoUsuario', TipoUsuarioViewSet)
urlpatterns = [

    path('api/', include(router.urls)),

]