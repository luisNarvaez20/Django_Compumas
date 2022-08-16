from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    id_Usuario = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=4, null = False, unique = True)
    nombre = models.CharField(max_length=10, null = False)
    telefono = models.CharField(max_length=70, null = False)
    email = models.CharField(max_length=15, null = True)
    Estado = models.CharField(max_length=70, null = False)
    Contraseña = models.CharField(max_length=15, null = True)

    def __str__(self): 
        return self.cedula