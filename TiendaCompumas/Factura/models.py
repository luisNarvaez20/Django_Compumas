from django.db import models

# Create your models here.
class Venta(models.Model):
    
    id_factura = models.AutoField(primary_key = True)
    subtotal = models.CharField(max_length=4, null = False, unique = True)
    descuento = models.CharField(max_length=10, null = False)
    iva = models.CharField(max_length=70, null = False)
    total = models.CharField(max_length=15, null = True)
    

    def __str__(self): 
        return self.id_factura