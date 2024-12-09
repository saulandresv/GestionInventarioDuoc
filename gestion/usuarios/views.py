from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages

def gestionUsuarios(request, usuario_id=None):
    # Si se proporciona un ID, estamos editando un usuario existente
    if usuario_id:
        usuario = get_object_or_404(Usuario, id=usuario_id)
        form = UsuarioForm(instance=usuario)  # Cargar datos existentes
    else:
        usuario = None  # Para un nuevo usuario
        form = UsuarioForm()

    if request.method == 'POST':
        if usuario:  # Caso de edición
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                messages.success(request, "Usuario actualizado exitosamente")
                return redirect('gestionUsuarios')
        else:  # Caso de creación
            form = UsuarioForm(request.POST)
            if form.is_valid():
                nuevo_usuario = form.save(commit=False)
                # Generar una contraseña automáticamente
                base_password = f"{nuevo_usuario.first_name[:1].lower()}{nuevo_usuario.last_name.lower()}{nuevo_usuario.fecha_nacimiento.day:02d}"
                nuevo_usuario.set_password(base_password)
                nuevo_usuario.save()
                messages.success(request, f"Usuario creado con contraseña: {base_password}")
                return redirect('gestionUsuarios')

    usuarios = Usuario.objects.all()  # Obtener todos los usuarios
    return render(request, 'usuarios/gestionUsuarios.html', {
        'form': form,
        'usuarios': usuarios,
        'usuario_id': usuario_id
    })

def eliminarUsuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Usuario eliminado exitosamente")
        return redirect('gestionUsuarios')
    return render(request, 'usuarios/eliminarUsuario.html', {'usuario': usuario})
