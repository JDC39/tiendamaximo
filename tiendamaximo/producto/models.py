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
    producto = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    

class Salida(models.Model):
    fechaSalida = models.DateTimeField()
    cantidadVenta = models.IntegerField()
    producto = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
