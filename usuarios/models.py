from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('OPER', 'Operador'),
        ('CONS', 'Consultor'),
    ]

    rol = models.CharField(max_length=5, choices=ROLES, default='OPER')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
