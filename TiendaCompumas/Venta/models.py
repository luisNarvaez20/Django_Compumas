from django.db import models

# Create your models here.
class Venta(models.Model):
    
    id_venta = models.AutoField(primary_key = True)
    fecha = models.CharField(max_length=4, null = False, unique = True)
    nombre = models.CharField(max_length=10, null = False)
    formadepago = models.CharField(max_length=70, null = False)
    Observacion = models.CharField(max_length=15, null = True)
    valor = models.CharField(max_length=70, null = False)
    

    def __str__(self): 
        return self.id_venta