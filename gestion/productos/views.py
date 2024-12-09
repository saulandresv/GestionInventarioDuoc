# gestion/productos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.http import JsonResponse
from proveedores.models import Proveedor

def gestionProductos(request, producto_id=None):
    if producto_id:
        producto = get_object_or_404(Producto, id=producto_id)
        form = ProductoForm(instance=producto)
    else:
        producto = None
        form = ProductoForm()

    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                messages.success(request, "Producto actualizado exitosamente.")
                return redirect('gestionProductos')
        else:
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Producto creado exitosamente.")
                return redirect('gestionProductos')

    productos = Producto.objects.all()
    return render(request, 'productos/gestionProductos.html', {
        'form': form,
        'productos': productos,
        'producto_id': producto_id,
    })

def eliminarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado exitosamente.")
        return redirect('gestionProductos')
    return render(request, 'productos/eliminarProducto.html', {'producto': producto})


def filtrar_proveedores(request):
    categoria = request.GET.get('categoria', None)
    if categoria:
        proveedores = Proveedor.objects.filter(tipo_proveedor=categoria).values('id', 'nombre_razon_social')
        return JsonResponse(list(proveedores), safe=False)
    return JsonResponse({'error': 'Categoría no proporcionada'}, status=400)