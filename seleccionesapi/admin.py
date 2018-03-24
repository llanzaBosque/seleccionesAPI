from django.contrib import admin

# Register your models here.
from seleccionesapi.models import Seleccion, Partido

admin.site.register(Seleccion)
admin.site.register(Partido)