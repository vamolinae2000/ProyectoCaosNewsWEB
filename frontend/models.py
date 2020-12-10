from django.db import models

# Create your models here.

class Usuario(models.Model):
    email=models.CharField(max_length=50, primary_key=True, verbose_name='email')
    nombre=models.CharField(max_length=50,verbose_name='nombre')
    password=models.CharField(max_length=50, verbose_name='password')
    
class Periodista(models.Model):
    idperiodista=models.AutoField(primary_key=True, verbose_name='idperiodista')
    nombre=models.CharField(max_length=50, verbose_name='nombre')
    email=email=models.CharField(max_length=50, verbose_name='email')
    password=models.CharField(max_length=50, verbose_name='password')

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name='ID Categoría')
    nombreCategoria=models.CharField(max_length=100, verbose_name='Nombre de Categoría')
    

class Imagen(models.Model):
    idImagen=models.AutoField(primary_key=True, verbose_name='ID Imagen')
    texto=models.CharField(max_length=120, verbose_name='Texto Descriptivo')
    nombre=models.CharField(max_length=50, verbose_name='Nombre Imagen')
    fechaRegistro=models.DateTimeField(verbose_name='Fecha y hora de Registro')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    periodista=models.ForeignKey(Periodista, on_delete=models.CASCADE)

