
from django.contrib import admin

from app.views import carrito
from .models import *


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['codigo','nombre','descripcion','precio','stock','tipo','imagen']
    search_fields = ['codigo']

class comuna(admin.ModelAdmin):
    list_display=['codigo','comuna']
    search_fields = ['codigo']

class cliente(admin.ModelAdmin):
    list_display=['codigo','nombre','apellido','rut','correo','numero','direccion','comuna']
    search_fields = ['codigo']

class CarritoAdmin(admin.ModelAdmin):
    list_display=['id','nombre_producto','precio_producto','imagen_producto', 'cantidad']
    search_fields = ['id']

class estadoSeguimientoAdmin(admin.ModelAdmin):
    list_display = ['id_estado','estado']
    search_fields= ['id_estado']

class SuscipcionAdmin(admin.ModelAdmin):
    list_display=['user','estado']
    search_fields = ['estado']

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['codigo','estado','nombre','precio','cantidad']
    search_fields = ['estado']




admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Comuna,comuna)
admin.site.register(Cliente,cliente)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Suscripcion, SuscipcionAdmin)
admin.site.register(Seguimiento, SeguimientoAdmin)
admin.site.register(EstadoSeguimiento,estadoSeguimientoAdmin)