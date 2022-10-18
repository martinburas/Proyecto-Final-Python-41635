from unicodedata import name
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Seleccion)

admin.site.register(Estadio)

admin.site.register(Copas)

admin.site.register(Prediccion)

admin.site.register(Avatar)