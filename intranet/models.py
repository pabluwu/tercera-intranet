from django.db import models
from django.contrib.auth.admin import User
from .validators import *


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()

class Citacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300, null=True)
    fecha = models.DateTimeField(null=True)
    lugar = models.CharField(max_length=100)
    tenida = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Licencia(models.Model):
    citacion = models.ForeignKey(Citacion, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_licencia = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("check_licencias", "Puede revisar todas las licencias"),
        ]

    def __str__(self):
        return self.motivo
    
class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tipo

class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=300)
    archivo = models.FileField(upload_to='docs/', validators=[file_size, validate_file_extension])
    nombre_original = models.CharField(max_length=500)
    fecha_documento = models.DateTimeField(auto_now_add=True)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
