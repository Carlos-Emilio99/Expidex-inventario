from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'rol', 'is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del sistema', {'fields': ('rol',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
