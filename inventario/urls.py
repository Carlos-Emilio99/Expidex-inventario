from django.urls import path
from .views import registrar_movimiento
from .views import listar_movimientos
from .views import exportar_movimientos_excel

urlpatterns = [
    path('registrar/', registrar_movimiento, name='registrar_movimiento'),
    path('listar/', listar_movimientos, name='listar_movimientos'),
    path('exportar_excel/', exportar_movimientos_excel, name='exportar_movimientos_excel'),
]
