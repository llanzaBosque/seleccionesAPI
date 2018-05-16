from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Representa una selección de fútbol que irá al mundial.
class Seleccion(models.Model):
    nombre = models.CharField(max_length=100)
    confederacion = models.CharField(max_length=100)
    tecnico = models.CharField(max_length=100)
    probabilidad = models.DecimalField(max_digits=11, decimal_places=2, null=0)
    ranking_fifa = models.IntegerField(null=0)
    descripcion = models.CharField(max_length=200)
    grupo = models.CharField(max_length=100)

    class Meta:
        ordering = ["probabilidad"]

    def __str__(self):
        return str(self.nombre)


# Representa un tipo de partido
class Tipo_Partido(models.Model):
    tipo = models.CharField(max_length=100)
    puntuacion = models.DecimalField(max_digits=11, decimal_places=2, null=0)

    def __str__(self):
        return (self.tipo)


# Representa un partido
class Partido(models.Model):
    seleccion_local = models.ForeignKey(Seleccion, related_name='local_fk', on_delete=models.CASCADE)
    seleccion_visitante = models.ForeignKey(Seleccion, related_name='visitante_fk', on_delete=models.CASCADE)
    seleccion_ganadora = models.ForeignKey(Seleccion, related_name='ganadora_fk', on_delete=models.CASCADE, null=True)
    fecha = models.DateField(blank=True, null=True)
    tipo = models.ForeignKey(Tipo_Partido, related_name='tipo_partido_fk', on_delete=models.CASCADE)
    penales = models.BooleanField

    def __str__(self):
        return '%s %s %s' % (self.fecha, self.seleccion_local, self.seleccion_visitante)


# Realiza el ordenamiento de las selecciones simulando
# los resultados del mundial.
class SeleccionesManager(models.Manager):
    def ordenar_selecciones(self):
        return

#  Retorna las selecciones por grupo
class SeleccionesGrupoAManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'A')

#  Retorna las selecciones por grupo B
class SeleccionesGrupoBManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'B')

#  Retorna las selecciones por grupo C
class SeleccionesGrupoCManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'C')

#  Retorna las selecciones por grupo D
class SeleccionesGrupoDManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'D')

#  Retorna las selecciones por grupo E
class SeleccionesGrupoEManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'E')

#  Retorna las selecciones por grupo F
class SeleccionesGrupoFManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'F')

#  Retorna las selecciones por grupo G
class SeleccionesGrupoGManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'G')

#  Retorna las selecciones por grupo H
class SeleccionesGrupoHManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(grupo = 'H')