from django.db import models

# Create your models here.
class FichaMantenimiento(models.Model):
    
    ficha_id = models.AutoField(primary_key = True)
    numero_ficha = models.CharField(max_length=4, null = False, unique = True)
    dispositivo = models.CharField(max_length=20, null = False)
    problema = models.CharField(max_length=70, null = False)
    fecha = models.CharField(max_length=15, null = True)

    def __str__(self):
        return self.numero_ficha