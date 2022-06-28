from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User

#SE ENCARGA DE HACER EL CRUD DESDE EL API
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscrito
        fields = '__all__'
