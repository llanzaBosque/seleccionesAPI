# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models








class Cuartos(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cuartos'




class Final(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'final'


class GrupoA(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_a'


class GrupoB(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_b'


class GrupoC(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_c'


class GrupoD(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_d'


class GrupoE(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_e'


class GrupoF(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_f'


class GrupoG(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_g'


class GrupoH(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo_h'


class Octavos(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'octavos'


class Podio(models.Model):
    id_seleccion = models.ForeignKey('SeleccionesapiSeleccion', models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=20)
    pos = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'podio'



class Semifinales(models.Model):
    id_seleccion = models.ForeignKey(SeleccionesapiSeleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=20)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'semifinales'


class Tercerlugar(models.Model):
    id_seleccion = models.ForeignKey(SeleccionesapiSeleccion, models.DO_NOTHING, db_column='id_seleccion')
    nombre = models.CharField(max_length=50)
    pos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tercerlugar'
