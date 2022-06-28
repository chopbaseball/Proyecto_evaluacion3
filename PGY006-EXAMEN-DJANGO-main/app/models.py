from operator import truediv
from pyexpat import model
from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    tipo = models.CharField(max_length=50)
    created_ad = models.DateField(auto_now_add = True)
    updated_ad = models.DateField(auto_now = True)
    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key = True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_ad = models.DateField(auto_now_add = True)
    updated_ad = models.DateField(auto_now = True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'

class TipoUsuario(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    tipo_usuario = models.CharField(max_length=50)
    created_ad = models.DateField(auto_now_add = True)
    updated_ad = models.DateField(auto_now = True)
    def __str__(self):
        return self.tipo_usuario
        
    class Meta:
        db_table = 'db_tipo_usuario'
        
class Usuario(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    created_ad = models.DateField(auto_now_add = True)
    updated_ad = models.DateField(auto_now = True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario'

class Carrito(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="carrito", null=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_item_carrito'

class Suscrito(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True, null=False)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_suscrito'


class Seguimiento(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'db_seguimiento'

class Historial(models.Model):
    orden = models.IntegerField()
    usuario = models.CharField(max_length=50)
    preciototal = models.IntegerField()
    estado = models.ForeignKey(Seguimiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario

    class Meta:
        db_table = 'db_historial'


class CarritoHistorico(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    codigo = models.IntegerField(null=True)
    codigoorden = models.IntegerField(null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="carrito", null=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_carrito_historico'