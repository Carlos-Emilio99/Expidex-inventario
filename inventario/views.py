from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MovimientoInventarioForm
from .models import MovimientoInventario

@login_required
def registrar_movimiento(request):
    if request.method == 'POST':
        form = MovimientoInventarioForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.usuario = request.user
            movimiento.save()
            return redirect('dashboard')
    else:
        form = MovimientoInventarioForm()
    
    return render(request, 'inventario/registrar_movimiento.html', {'form': form})

from django.db.models import Q
from productos.models import Producto
from django.utils import timezone

@login_required
def listar_movimientos(request):
    movimientos = MovimientoInventario.objects.select_related('producto', 'usuario').order_by('-fecha')

    tipo = request.GET.get('tipo')
    producto_id = request.GET.get('producto')
    desde = request.GET.get('desde')
    hasta = request.GET.get('hasta')

    if tipo:
        movimientos = movimientos.filter(tipo=tipo)
    
    if producto_id:
        movimientos = movimientos.filter(producto__id=producto_id)

    if desde:
        movimientos = movimientos.filter(fecha__date__gte=desde)
    
    if hasta:
        movimientos = movimientos.filter(fecha__date__lte=hasta)

    productos = Producto.objects.all()

    context = {
        'movimientos': movimientos,
        'productos': productos,
        'tipo': tipo,
        'producto_id': producto_id,
        'desde': desde,
        'hasta': hasta,
    }
    return render(request, 'inventario/listar_movimientos.html', context)


import datetime
from django.http import HttpResponse
import openpyxl
from openpyxl.styles import Font

@login_required
def exportar_movimientos_excel(request):
    movimientos = MovimientoInventario.objects.select_related('producto', 'usuario').order_by('-fecha')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Movimientos"

    # Encabezados
    encabezados = ['Producto', 'Tipo', 'Cantidad', 'Usuario', 'Fecha', 'Observaciones']
    ws.append(encabezados)
    for col in ws.iter_cols(min_row=1, max_row=1):
        for cell in col:
            cell.font = Font(bold=True)

    # Filas
    for m in movimientos:
        ws.append([
            m.producto.nombre,
            m.get_tipo_display(),
            m.cantidad,
            m.usuario.username if m.usuario else "—",
            m.fecha.strftime("%d/%m/%Y %H:%M"),
            m.observaciones or "-"
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    fecha_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"movimientos_{fecha_actual}.xlsx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    wb.save(response)
    return response
