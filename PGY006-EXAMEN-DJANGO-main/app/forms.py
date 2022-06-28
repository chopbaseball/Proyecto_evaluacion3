from dataclasses import fields
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creamos un template del formulario

class FormularioUserRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=5,max_length=20)
    precio = forms.IntegerField(min_value=400)
    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen']

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['codigo', 'nombre','usuario','precio','imagen', 'cantidad']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class SuscritoForm(ModelForm):
    class Meta:
        model = Suscrito
        fields = ['nombre','estado']

class HistorialForm(ModelForm):
    class Meta:
        model = Historial
        fields = ['estado']

class CarritoHistoricoForm(ModelForm):
    class Meta:
        model = CarritoHistorico
        fields = ['nombre','usuario','codigo','precio','imagen', 'cantidad']

class SeguimientoForm(ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['codigo','estado']