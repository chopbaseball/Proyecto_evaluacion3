from re import search
from django.contrib import admin
from .models import *
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen']
    search_fields = ['codigo']
    list_per_page = 3

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','usuario','precio','imagen', 'cantidad']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(Carrito)

class SuscritoAdmin(admin.ModelAdmin):
    list_display = ['nombre','estado']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(Suscrito)

class HistorialAdmin(admin.ModelAdmin):
    list_display = ['orden','usuario','preciototal', 'estado']
    search_fields = ['orden']
    list_per_page = 3

admin.site.register(Seguimiento)
admin.site.register(Historial, HistorialAdmin)

class CarritoHistoricoAdmin(admin.ModelAdmin):
    list_display = ['nombre','usuario','codigo','precio','imagen', 'cantidad']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(CarritoHistorico)