from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from usuarios.decorators import admin_required
from usuarios import views as usuarios_views
from proveedores import views as proveedores_views
from productos import views as productos_views
from inventario import views as inventario_views
from login import views as login_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Wrap each view with login_required (except login)
    path('gestionUsuarios/', login_required(admin_required(usuarios_views.gestionUsuarios)), name='gestionUsuarios'),
    path('gestionUsuarios/<int:usuario_id>/', login_required(admin_required(usuarios_views.gestionUsuarios)), name='gestionUsuarios'),
    path('gestionUsuarios/eliminar/<int:usuario_id>/', login_required(admin_required(usuarios_views.eliminarUsuario)), name='eliminarUsuario'),

    # Gestión de Proveedores
    path('proveedores/', login_required(admin_required(proveedores_views.gestionProveedores)), name='gestionProveedores'),
    path('proveedores/<int:proveedor_id>/', login_required(admin_required(proveedores_views.gestionProveedores)), name='gestionProveedores'),
    path('proveedores/eliminar/<int:proveedor_id>/', login_required(admin_required(proveedores_views.eliminarProveedor)), name='eliminarProveedor'),
    
    # Gestión de Productos
    path('productos/', login_required(admin_required(productos_views.gestionProductos)), name='gestionProductos'),
    path('productos/<int:producto_id>/', login_required(admin_required(productos_views.gestionProductos)), name='gestionProductos'),
    path('productos/eliminar/<int:producto_id>/', login_required(admin_required(productos_views.eliminarProducto)), name='eliminarProducto'),
    path('productos/filtrar_proveedores/', login_required(admin_required(productos_views.filtrar_proveedores)), name='filtrarProveedores'),

    # Gestión de Inventario
    path('inventario/', login_required(inventario_views.gestionInventario), name='gestionInventario'),
    path('añadir/', login_required(inventario_views.añadirProductoInventario), name='añadirProductoInventario'),
    path('modificar/', login_required(inventario_views.modificarCantidad), name='modificarCantidad'),

    # Gestión de historial inventario
    path('historial/', login_required(inventario_views.historial), name='historial'),

    # login (No login required for this)
    path('login/', login_views.login_view, name='login'),
    # logOUT
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
