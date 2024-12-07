from django.db import models

class Proveedor(models.Model):
    nombre_razon_social = models.CharField(max_length=100)
    
    class TipoProveedor(models.TextChoices):
        ASEO = 'Aseo', 'Aseo'
        DESPENSA = 'Despensa', 'Despensa'
        CONGELADOS = 'Congelados', 'Congelados'
        CUIDADO_PERSONAL = 'Cuidado Personal', 'Cuidado Personal'
    
    tipo_proveedor = models.CharField(
        max_length=16,
        choices=TipoProveedor.choices,
        default=TipoProveedor.ASEO,
    )
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_razon_social
