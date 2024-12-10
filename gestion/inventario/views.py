from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario
from productos.models import Producto
from django.contrib import messages
from inventario.models import HistorialInventario
def gestionInventario(request):
    # Productos registrados en el inventario
    inventarios = Inventario.objects.select_related('producto').all()
    # Productos que no están registrados en el inventario
    productos_no_registrados = Producto.objects.exclude(id__in=inventarios.values('producto_id'))
    return render(request, 'inventario/gestionInventario.html', {
        'inventarios': inventarios,
        'productos_no_registrados': productos_no_registrados,
    })

def añadirProductoInventario(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))
        producto = get_object_or_404(Producto, id=producto_id)

        # Crear o actualizar la entrada en el inventario
        inventario, creado = Inventario.objects.get_or_create(producto=producto)
        inventario.cantidad_disponible += cantidad
        inventario.save()

        return redirect('gestionInventario')



def modificarCantidad(request):
    """
    Modifica o agrega un producto al inventario.
    """
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad_nueva = int(request.POST.get('cantidad_disponible'))
        descripcion = request.POST.get('descripcion')

        # Verificar si el producto existe
        producto = get_object_or_404(Producto, id=producto_id)

        # Crear o actualizar el inventario para el producto seleccionado
        inventario, created = Inventario.objects.get_or_create(producto=producto)
        inventario.cantidad_disponible = cantidad_nueva
        inventario.save()

        # Mensaje de éxito
        if created:
            messages.success(request, f"Producto '{producto.nombre_producto}' agregado al inventario con éxito.")
        else:
            messages.success(request, f"Cantidad de '{producto.nombre_producto}' actualizada correctamente.")
        
        return redirect('gestionInventario')

def historial(request):
    if request.method == 'POST':
        pass
    historialInventario = HistorialInventario.objects.exclude(id__in=Inventario.objects.values('id'))
    return render(request, 'inventario/historialInventario.html', {
        'historialInventario': historialInventario,
    })