from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    imagen = models.ImageField(upload_to='carpeta de imagenes', verbose_name='Imagen', null=True)
    telefono = models.CharField(max_length=100, verbose_name='telefono')
    genero = models.CharField(max_length=100, verbose_name='genero')
    fechaN = models.CharField(max_length=100, verbose_name='fecha de nacimiento')
    tipoUsuarioID = models.CharField(max_length=100, verbose_name='tipoUsuarioID')
    login = models.CharField(max_length=100, verbose_name='login')
    password = models.CharField(max_length=100, verbose_name='password')
    usuarioStatus = models.CharField(max_length=100, verbose_name='status')

    def __str__(self):
        fila = "Nombre " + self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
