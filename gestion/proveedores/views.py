from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib import messages

def gestionProveedores(request, proveedor_id=None):
    if proveedor_id:
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        form = ProveedorForm(instance=proveedor)
    else:
        proveedor = None
        form = ProveedorForm()

    if request.method == 'POST':
        if proveedor:
            form = ProveedorForm(request.POST, instance=proveedor)
            if form.is_valid():
                form.save()
                messages.success(request, "Proveedor actualizado exitosamente.")
                return redirect('gestionProveedores')
        else:
            form = ProveedorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Proveedor creado exitosamente.")
                return redirect('gestionProveedores')

    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/gestionProveedores.html', {
        'form': form,
        'proveedores': proveedores,
        'proveedor_id': proveedor_id,
    })


def eliminarProveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, "Proveedor eliminado exitosamente.")
        return redirect('gestionProveedores')
    return render(request, 'proveedores/eliminarProveedor.html', {'proveedor': proveedor})
