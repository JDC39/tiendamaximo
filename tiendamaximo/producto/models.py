from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=1000)
    articulo=models.CharField(max_length=1000)
    ingreso=models.IntegerField()
    salida=models.IntegerField()
    stock= models.IntegerField()

class Entrada(models.Model):
    fechaEntrada = models.DateTimeField() 
    cantidadComprada = models.IntegerField() 
    
c    
    

