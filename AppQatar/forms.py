from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppQatar.models import Avatar, Estadio, Seleccion
import datetime


class SelForm(forms.ModelForm):
    class Meta:
        model = Seleccion
        fields = ['pais', 'continente','fecha', 'imagen2']

class EstForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nombre', 'ciudad', 'imagen']

class CopForm(forms.Form):   
    selecc= forms.CharField()
    cantCopas= forms.IntegerField()
    ultimaCopa= forms.IntegerField()

class PredForm(forms.Form):
    ganadora=forms.CharField(max_length=40)
    segunda=forms.CharField(max_length=40)


#REFERIDO A LA ADMINISTRACIÓN DE USUARIOS
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    password1= forms.CharField(label="Contreseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repite la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repite la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model= Avatar
        fields= ["imagen"]