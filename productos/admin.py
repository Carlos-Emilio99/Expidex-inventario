from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'categoria', 'unidad_medida', 'cantidad_disponible')
    search_fields = ('nombre', 'codigo', 'categoria')
    list_filter = ('categoria', 'unidad_medida')
