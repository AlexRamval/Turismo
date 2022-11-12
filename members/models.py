from django.contrib.auth.models import User
from django.db import models

class TipoUsuario(models.Model):
    tipousuarioid = models.AutoField(db_column='tipoUsuarioID', primary_key=True)
    tipousuariodescripcion = models.CharField(db_column='tipoUsuarioDescripcion', max_length=40, blank=True, null=True)
    tipousuariostatus = models.IntegerField(db_column='tipoUsuarioStatus', blank=True, null=True)

    def __str__(self):
        fila = "" + self.tipousuariodescripcion
        return fila
    class Meta:
        managed = False
        db_table = 'tipo_usuario'
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    imagen = models.ImageField(upload_to='carpeta de imagenes', verbose_name='Imagen', null=True)
    telefono = models.CharField(max_length=100, verbose_name='telefono')
    genero = models.CharField(max_length=100, verbose_name='genero')
    fechaN = models.CharField(max_length=100, verbose_name='fecha de nacimiento')
    tipoUsuarioID = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipoUsuarioID', blank=True,verbose_name='Tipo de Usuario', null=True)
    login = models.CharField(max_length=100, verbose_name='login')
    password = models.CharField(max_length=100, verbose_name='password')
    usuarioStatus = models.CharField(max_length=100, verbose_name='status')

    def __str__(self):
        fila = "Nombre " + self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class CategoriaTurismo(models.Model):
    catturid = models.AutoField(db_column='catTurID', primary_key=True)  # Field name made lowercase.
    catturdescrip = models.CharField(db_column='catTurDescrip', max_length=40, blank=True,verbose_name='Categoría', null=True)  # Field name made lowercase.
    catturstatus = models.IntegerField(db_column='catTurStatus', blank=True,verbose_name='Estatus', null=True)  # Field name made lowercase.
    def __str__(self):
        fila = "" + self.catturdescrip
        return fila
    class Meta:
        managed = False
        db_table = 'categoria_turismo'
    def delete(self, using=None, keep_parents=False):
        super().delete()

class PuntoTuristico(models.Model):
    puntoID = models.AutoField(primary_key=True)
    puntoNombre = models.CharField(max_length=100, verbose_name='nombre')
    puntoDir = models.CharField(max_length=100, verbose_name='Dirección')
    url = models.ImageField(upload_to='carpeta de imagenes', verbose_name='Imagen', null=True)
    puntoRef = models.CharField(max_length=100, verbose_name='Referencia de dirección')
    puntoCol = models.CharField(max_length=100, verbose_name='Colonia')
    puntoCP = models.CharField(max_length=100, verbose_name='Código postal')
    puntoLocalidad = models.CharField(max_length=100, verbose_name='Localidad')
    puntoInfromacion = models.TextField(max_length=500, verbose_name='Información')
    puntoHorario = models.CharField(max_length=100, verbose_name='Horario')
    puntoNumVisitas = models.CharField(max_length=100, verbose_name='Número de visitas')
    puntoCatID = models.ForeignKey(CategoriaTurismo, models.DO_NOTHING, db_column='puntoCatID', blank=True,verbose_name='Categoría', null=True)
    puntoObsverv = models.CharField(max_length=100, verbose_name='Observaciones')
    puntoStatus = models.CharField(max_length=100, verbose_name='Estatus')

    def __str__(self):
        fila = "" + self.puntoNombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.url.storage.delete(self.url.name)
        super().delete()

class CategoriaEvento(models.Model):
    cateventoid = models.AutoField(db_column='catEventoID', primary_key=True)  # Field name made lowercase.
    cateventodescrip = models.CharField(db_column='catEventoDescrip', max_length=40, blank=True,verbose_name='Categoría', null=True)  # Field name made lowercase.
    cateventostatus = models.IntegerField(db_column='catEventoStatus', blank=True,verbose_name='Estatus', null=True)  # Field name made lowercase.
    def __str__(self):
        fila = "" + self.cateventodescrip
        return fila
    class Meta:
        managed = False
        db_table = 'categoria_evento'
    def delete(self, using=None, keep_parents=False):
        super().delete()

class Evento(models.Model):
    eventoid = models.AutoField(db_column='eventoID', primary_key=True)  # Field name made lowercase.
    eventonombre = models.CharField(db_column='eventoNombre', max_length=40, blank=True, null=True)  # Field name made lowercase.
    organizid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='organizID', blank=True,verbose_name='Nombre del organizador', null=True)  # Field name made lowercase.
    eventopuntoid = models.ForeignKey('PuntoTuristico', models.DO_NOTHING, db_column='eventoPuntoID', blank=True,verbose_name='Lugar del evento', null=True)  # Field name made lowercase.
    eventoscantdias = models.IntegerField(db_column='eventosCantDias', blank=True, null=True)  # Field name made lowercase.
    eventofechainicio = models.DateField(db_column='eventoFechaInicio', blank=True, null=True)  # Field name made lowercase.
    eventofechafinal = models.DateField(db_column='eventoFechaFinal', blank=True, null=True)  # Field name made lowercase.
    eventohorario = models.CharField(db_column='eventoHorario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eventocategid = models.ForeignKey(CategoriaEvento, models.DO_NOTHING, db_column='eventoCategID', blank=True,verbose_name='Categoría', null=True)  # Field name made lowercase.
    eventoobserv = models.CharField(db_column='eventoObserv', max_length=200, blank=True, null=True)  # Field name made lowercase.
    eventostatus = models.IntegerField(db_column='eventoStatus', blank=True, null=True)  # Field name made lowercase.
    telefonocontacto = models.CharField(db_column='telefonoContacto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    url = models.ImageField(upload_to='carpeta de imagenes', verbose_name='Imagen', null=True)  # Field name made lowercase.
    multimid = models.IntegerField(db_column='multimID', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'evento'
    def __str__(self):
        fila = "" + self.eventonombre
        return fila
    def delete(self, using=None, keep_parents=False):
        self.url.storage.delete(self.url.name)
        super().delete()

class usuario(User):

    def __str__(self):
        return self.username