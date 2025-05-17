from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=20)
    cantidad_disponible = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
