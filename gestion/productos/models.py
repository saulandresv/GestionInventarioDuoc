from django.db import models
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    
    class Categoria(models.TextChoices):
        ASEO = 'aseo', 'Aseo'
        DESPENSA = 'Despensa', 'Despensa'
        CONGELADOS = 'Congelados', 'Congelados'
        CUIDADO_PERSONAL = 'Cuidado Personal', 'Cuidado Personal'
    
    categoria = models.CharField(
        max_length=16,
        choices=Categoria.choices,
        default=Categoria.ASEO,
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(
        'proveedores.Proveedor',
        on_delete=models.PROTECT,
        related_name='productos'
    )
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
