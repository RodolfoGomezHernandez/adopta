from django.db import models

# Create your models here.
class Mascota(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kg")
    estatura = models.DecimalField(max_digits=5, decimal_places=2, help_text="Estatura en cm")
    descripcion = models.TextField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    comuna = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True) # Guarda la fecha automáticamente

    def __str__(self):
        return f"Contacto de {self.nombre} - {self.correo}"