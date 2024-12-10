from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventario
from productos.models import Producto
from django.contrib import messages
from inventario.models import HistorialInventario
from .forms import HistorialInventarioForm

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
    Modifica o agrega un producto al inventario y registra la acción en HistorialInventario.
    """
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad_nueva = int(request.POST.get('cantidad_disponible'))
        descripcion = request.POST.get('descripcion')

        # Verificar si el producto existe
        producto = get_object_or_404(Producto, id=producto_id)

        # Obtener o crear el inventario para el producto
        inventario, created = Inventario.objects.get_or_create(producto=producto)
        
        # Guardar la cantidad anterior antes de actualizar
        cantidad_anterior = inventario.cantidad_disponible

        # Actualizar la cantidad disponible en el inventario
        inventario.cantidad_disponible = cantidad_nueva
        inventario.save()

        # Calcular la cantidad cambiada
        cantidad_cambiada = cantidad_nueva - cantidad_anterior

        # Crear registro en HistorialInventario
        HistorialInventario.objects.create(
            inventario=inventario,
            cantidad_cambiada=cantidad_cambiada,
            descripcion=descripcion,
            usuario=request.user
        )

        # Mensaje de éxito
        if created:
            messages.success(request, f"Producto '{producto.nombre_producto}' agregado al inventario con éxito.")
        else:
            messages.success(request, f"Cantidad de '{producto.nombre_producto}' actualizada correctamente.")

        return redirect('gestionInventario')

def historial(request, historial_id=None):
    # Si se proporciona un ID, estamos editando un historial existente
    if historial_id:
        registro = get_object_or_404(HistorialInventario, id=historial_id)
        form = HistorialInventarioForm(instance=registro)  # Cargar datos existentes
    else:
        registro = None  # Para un nuevo historial
        form = HistorialInventarioForm()

    if request.method == 'POST':
        if registro:  # Caso de edición
            form = HistorialInventarioForm(request.POST, instance=registro)
            if form.is_valid():
                historial_actualizado = form.save(commit=False)
                # Aquí puedes modificar más campos si es necesario
                historial_actualizado.save()
                messages.success(request, "Historial de inventario actualizado exitosamente")
                return redirect('historial')
        else:  # Caso de creación
            form = HistorialInventarioForm(request.POST)
            if form.is_valid():
                nuevo_historial = form.save(commit=False)
                # Asignar usuario actual al historial
                nuevo_historial.usuario = request.user
                # Si quieres asignar inventario y cantidad_cambiada aquí, hazlo:
                # Por ejemplo, asumiendo inventario_id o cantidad_cambiada vienen en POST
                # nuevo_historial.inventario = Inventario.objects.get(id=algún_id)
                # nuevo_historial.cantidad_cambiada = cantidad
                nuevo_historial.save()
                messages.success(request, "Historial de inventario creado exitosamente")
                return redirect('historial')

    # Obtener todos los registros de historial de inventario
    historialInventario = (
        HistorialInventario.objects
        .select_related('inventario', 'inventario__producto', 'usuario')
        .all()
    )

    return render(request, 'inventario/historialInventario.html', {
        'historialInventario': historialInventario,
        'form': form,
        'historial_id': historial_id
    })