from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.conf import settings

class Inventario(models.Model):
    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.PROTECT,  # Evita la eliminación en cascada
        related_name='inventarios'
    )
    cantidad_disponible = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre_producto} - Cantidad: {self.cantidad_disponible}"

class HistorialInventario(models.Model):
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.PROTECT,
        related_name='historiales'
    )
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    cantidad_cambiada = models.IntegerField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='cambios_inventario'
    )

    def __str__(self):
        return f"Cambio en {self.inventario.producto.nombre_producto} por {self.usuario.username} el {self.fecha_cambio}"
