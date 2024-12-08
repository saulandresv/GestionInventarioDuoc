from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages

def gestionUsuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False) 
            base_password = f"{usuario.first_name[:1].lower()}{usuario.last_name.lower()}{usuario.fecha_nacimiento.day:02d}"
            usuario.set_password(base_password)
            usuario.save()
            messages.success(request, f"Usuario creado con contraseña: {base_password}")
            return redirect('gestionUsuarios')
    else:
        form = UsuarioForm()
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/gestionUsuarios.html', {'form': form, 'usuarios': usuarios})
