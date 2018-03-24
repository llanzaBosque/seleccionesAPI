from django.db import models

# Representa una selección de fútbol que irá al mundial.
class Seleccion(models.Model):
    nombre = models.CharField(max_length=40)
    confederacion = models.CharField(max_length=40)
    tecnico = models.CharField(max_length=40)
    probabilidad = models.DecimalField(max_digits=11, decimal_places=2, null=0)
    goles = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    grupo = models.CharField(max_length=40)

    def __unicode__(self):
        return str(self.nombre)

    def __str__(self):
        return str(self.nombre)


# Representa un partido
class Partido(models.Model):
    seleccion_local = models.ForeignKey(Seleccion, related_name='local_fk', on_delete=models.CASCADE)
    seleccion_visitante = models.ForeignKey(Seleccion, related_name= 'visitante_fk',on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
