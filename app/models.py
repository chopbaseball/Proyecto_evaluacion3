from re import T
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo_productos = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_productos
    
    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    create_at = models.DateField(auto_now_add=True) #guarda producto con la fecha actual
    update_at = models.DateField(auto_now=True)

    #para separar las imagenes se cambia el nombre en upload to

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'db_producto'

class Carrito(models.Model):
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to ="Carrito", null= True)
    usuario = models.CharField(max_length=200)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_Carrito'

class Comuna(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    comuna = models.CharField(max_length=25)
    def __str__(self):
        return self.comuna
    
    class Meta:
        db_table = 'db_comuna'

class Cliente(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=13)
    correo = models.CharField(max_length=100)
    numero = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'db_cliente'

class Suscripcion(models.Model):
    user = models.CharField(max_length=200,null=False, primary_key=True)
    estado = models.BooleanField()
    
    def __str__(self):
        return self.estado
    class Meta:
        db_table = 'db_Suscripcion'


class EstadoSeguimiento(models.Model):
    id_estado = models.IntegerField(null=False, primary_key=True)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado
    
    class Meta:
        db_table = 'db_EstadoSeguimiento'

class Historial(models.Model):
    
    orden = models.IntegerField()
    precio = models.IntegerField()
    usuario = models.CharField(max_length=200)
    estado = models.ForeignKey(EstadoSeguimiento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.orden
    
    class Meta:
        db_table = 'db_Historial'

class CarritoHist(models.Model):
    
    codigo_his = models.IntegerField()
    nombre_his = models.CharField(max_length=100)
    precio_hist = models.IntegerField()
    imagen_hist = models.ImageField(upload_to ="Carrito", null= True)
    usuario_hist = models.CharField(max_length=200)
    cantidad_hist = models.IntegerField()
    oorden = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'db_CarritoHist'



class Seguimiento(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    codigoProducto = models.IntegerField(null=False)
    estado = models.ForeignKey(EstadoSeguimiento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    

    def __str__(self):
        return self.codigo
    
    class Meta:
        db_table = 'db_seguimiento'
    
