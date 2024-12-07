from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    fecha_nacimiento = models.DateField()
    rut = models.CharField(max_length=12, unique=True)
    ROL_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Usuario general', 'Usuario general'),
    ]
    rol = models.CharField(max_length=15, choices=ROL_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Use a custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set_permissions",  # Use a custom related_name
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
