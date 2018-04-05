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
        return(self.tipo)

# Representa un partido
class Partido(models.Model):
    seleccion_local = models.ForeignKey(Seleccion, related_name='local_fk', on_delete=models.CASCADE)
    seleccion_visitante = models.ForeignKey(Seleccion, related_name= 'visitante_fk',on_delete=models.CASCADE)
    seleccion_ganadora = models.ForeignKey(Seleccion, related_name='ganadora_fk', on_delete=models.CASCADE)
    fecha = models.DateField(blank = True, null=True)
    tipo = models.ForeignKey(Tipo_Partido, related_name='tipo_partido_fk', on_delete=models.CASCADE)
    penales = models.BooleanField

    #Otorga el puntaje correspondiente a las selecciones
    #def save(self, force_insert=False, force_update=False, using=None,
    #         update_fields=None):
        #Trigger
        #sel_local = Seleccion.objects.get(id = self.seleccion_local)
        #local.probabilidad = 50
        #Fin del trigger

    #   return super(Partido, self).save()

    def __str__(self):
        return '%s %s %s' %(self.fecha, self.seleccion_local, self.seleccion_visitante)

@receiver(post_save, sender=User)
def partido_is_created(sender, instance, created, **kwargs):
    if created:
        instance.seleccion_local.probabilidad = 50