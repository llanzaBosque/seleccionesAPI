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


# Representa las selecciones en cuartos de final
class Cuartos(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cuartos'

# Representa las selecciones que jugarán la final
class Final(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'final'


class GrupoA(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_a'


class GrupoB(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_b'


class GrupoC(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_c'


class GrupoD(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_d'


class GrupoE(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_e'


class GrupoF(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_f'


class GrupoG(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_g'


class GrupoH(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_h'


class Octavos(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'octavos'


class Podio(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=20)
    pos = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'podio'

class Semifinales(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=20)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'semifinales'


class Tercerlugar(models.Model):
    id_seleccion = models.ForeignKey(Seleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tercerlugar'