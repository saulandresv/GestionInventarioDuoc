from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Primero verifica si el usuario está autenticado
        if not request.user.is_authenticated:
            return redirect('login')

        # Ahora verifica el rol
        if request.user.rol == 'Administrador':
            return view_func(request, *args, **kwargs)
        else:
            # Si el usuario no es administrador, puede:
            # - Redirigir a una página de error o
            # - Mostrar un mensaje personalizado
            # Aquí mostramos un error 403 por defecto
            raise PermissionDenied("No tienes permiso para acceder a esta página.")
    return _wrapped_view
