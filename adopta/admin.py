from django.contrib import admin
from .models import Mascota, Contacto # Importamos los modelos

# Register your models here.

# Registramos los modelos para que aparezcan en el admin
admin.site.register(Mascota)
admin.site.register(Contacto)