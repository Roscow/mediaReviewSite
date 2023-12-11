from django.db import models


class AnalisisDiario(models.Model):
    medio = models.ForeignKey('Medio', models.DO_NOTHING, db_column='medio', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    buenas = models.IntegerField()
    malas = models.IntegerField()
    neutra = models.IntegerField()
    total = models.IntegerField()
    data_scraping = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analisis_diario'


class AnalisisGeneral(models.Model):
    fecha = models.DateField(blank=True, null=True)
    buenas = models.IntegerField()
    malas = models.IntegerField()
    neutra = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analisis_general'


class Contexto(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'contexto'


class Medio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion_web = models.CharField(max_length=1000)
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'medio'


class MedioDiario(models.Model):
    medio = models.ForeignKey(Medio, models.DO_NOTHING, db_column='medio', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medio_diario'


class Noticia(models.Model):
    medio_diario = models.ForeignKey(MedioDiario, models.DO_NOTHING, db_column='medio_diario')
    titular = models.CharField(max_length=200)
    contexto = models.ForeignKey(Contexto, models.DO_NOTHING, db_column='contexto')

    class Meta:
        managed = False
        db_table = 'noticia'


class Region(models.Model):
    nombre = models.CharField(max_length=100)
    romano = models.CharField(max_length=10)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region'
