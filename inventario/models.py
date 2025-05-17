from django.db import models
from django.contrib.auth import get_user_model
from productos.models import Producto

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo afecta al crear (no al editar)
            if self.tipo == 'ENTRADA':
                self.producto.cantidad_disponible += self.cantidad
            elif self.tipo == 'SALIDA':
                self.producto.cantidad_disponible -= self.cantidad
            self.producto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} ({self.cantidad})"
