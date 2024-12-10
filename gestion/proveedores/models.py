from django.db import models

class Proveedor(models.Model):
    nombre_razon_social = models.CharField(max_length=100, verbose_name="Nombre o Razón Social")

    class TipoProveedor(models.TextChoices):
        ASEO = 'Aseo', 'Aseo'
        DESPENSA = 'Despensa', 'Despensa'
        CONGELADOS = 'Congelados', 'Congelados'
        CUIDADO_PERSONAL = 'Cuidado Personal', 'Cuidado Personal'

    tipo_proveedor = models.CharField(
        max_length=16,
        choices=TipoProveedor.choices,
        blank=False,
    )

    rut = models.CharField(
        max_length=12, 
        unique=True, 
        verbose_name="RUT"
    )
    direccion = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Dirección"
    )
    telefono = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name="Teléfono"
    )
    email = models.EmailField(
        max_length=100, 
        unique=True, 
        blank=True, 
        null=True, 
        verbose_name="Correo Electrónico"
    )
    notas = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Notas o Comentarios"
    )
    creado_en = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return self.nombre_razon_social
