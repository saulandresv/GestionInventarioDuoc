"""
URL configuration for gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views as usuarios_views
from proveedores import views as proveedores_views
from productos import views as productos_views
from inventario import views as inventario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionUsuarios/', usuarios_views.gestionUsuarios, name='gestionUsuarios'),
    path('gestionUsuarios/<int:usuario_id>/', usuarios_views.gestionUsuarios, name='gestionUsuarios'),
    path('gestionUsuarios/eliminar/<int:usuario_id>/', usuarios_views.eliminarUsuario, name='eliminarUsuario'),

    # Gestión de Proveedores
    path('proveedores/', proveedores_views.gestionProveedores, name='gestionProveedores'),
    path('proveedores/<int:proveedor_id>/', proveedores_views.gestionProveedores, name='gestionProveedores'),
    path('proveedores/eliminar/<int:proveedor_id>/', proveedores_views.eliminarProveedor, name='eliminarProveedor'),
    
     # Gestión de Productos
    path('productos/', productos_views.gestionProductos, name='gestionProductos'),
    path('productos/<int:producto_id>/', productos_views.gestionProductos, name='gestionProductos'),
    path('productos/eliminar/<int:producto_id>/', productos_views.eliminarProducto, name='eliminarProducto'),
    path('productos/filtrar_proveedores/', productos_views.filtrar_proveedores, name='filtrarProveedores'),

      # Gestión de Inventario
    path('inventario/', inventario_views.gestionInventario, name='gestionInventario'),
    path('añadir/', inventario_views.añadirProductoInventario, name='añadirProductoInventario'),
    path('modificar/', inventario_views.modificarCantidad, name='modificarCantidad'),

    # Gestión de historial inventario
    path('historial/', inventario_views.historial, name='historial'),
]

