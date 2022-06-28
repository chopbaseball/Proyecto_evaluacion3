
from django import forms
from django.forms import ModelForm
from .models import * 

#creamos un template del fromulario

from django import forms
from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#creamos un template del fromulario

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=10,max_length=200)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','precio','stock','tipo','imagen']

class ClienteForm(ModelForm):
    nombre = forms.CharField(min_length=5,max_length=200)
    rut = forms.CharField(min_length=8,max_length=13)

    class Meta:
        model= Cliente
        fields = ['codigo','nombre','apellido','rut','correo','numero','direccion','comuna']

class FormularioUserResgistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class EstadoSeguimientoForm (ModelForm):
    estado = forms.CharField(min_length=5,max_length=30)
    class Meta:
        model = EstadoSeguimiento
        fields = ['id_estado','estado']

class SeguimientoForm(ModelForm):
    

    class Meta:
        model = Seguimiento
        fields = ['codigo','estado']
   