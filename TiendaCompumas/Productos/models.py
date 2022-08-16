from django.db import models

# Create your models here.
class Producto(models.Model):
    
    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=4, null = False, unique = True)
    cantidad = models.IntegerField(max_length=10, null = False)
    precio = models.Double(max_length=70, null = False)


    def __str__(self): 
        return self.nombre
