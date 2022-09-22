from importlib.util import module_from_spec
import this
from django.db import models
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    descripcion=models.TextField()
    idcategoria=models.ForeignKey('self',null=True, on_delete=models.CASCADE,related_name="categoria")
    def __str__(self) -> str:
        return self.nombre
class Fabricante(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    telefonos=models.TextField()
    responsable=models.TextField()
    direccion=models.TextField()
    correo=models.TextField()
    
class Producto(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    codigo=models.CharField(max_length=100)
    descripcion=models.TextField()
    idcategoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    idfabricante=models.ForeignKey(Fabricante,on_delete=models.CASCADE)