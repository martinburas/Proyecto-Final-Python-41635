from django.db import models
from django.contrib.auth.models import User
import datetime


class Seleccion(models.Model):
    pais=models.CharField(max_length=60)
    continente= models.CharField(max_length=60)
    fecha=models.DateField("Fecha de su primer partido (YYYY-MM-DD)", blank=True, null=True)
    imagen2= models.ImageField("Bandera", upload_to ='banderas', null=True, blank=True)

    def __str__(self):
        return self.pais


class Estadio(models.Model):
    nombre= models.CharField("Nombre del estadio", max_length=60)
    ciudad= models.CharField("Ciudad en la que se encuentra el estadio", max_length=60)
    imagen= models.ImageField("Imagen del estadio", upload_to ='estadios', null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Copas(models.Model):
    selecc= models.CharField("Selección", max_length=60)
    cantCopas= models.IntegerField("Cantidad de copas")
    ultimaCopa= models.IntegerField('Año de la última copa conseguida ("0" si no ha ganado aún)')
    
    def __str__(self):
        return self.selecc


class Prediccion(models.Model):
    autor=models.CharField(max_length=40, default="")
    ganadora=models.CharField("Selección campeona",max_length=40)
    segunda=models.CharField("Selección subcampeona",max_length=40)
    hoy=models.DateField(default=datetime.date.today)


class Avatar(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f'Avatar de {self.usuario}'