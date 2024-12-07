# Generated by Django 5.1.4 on 2024-12-07 22:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_disponible', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventarios', to='productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cambio', models.DateTimeField(auto_now_add=True)),
                ('cantidad_cambiada', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cambios_inventario', to=settings.AUTH_USER_MODEL)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historiales', to='inventario.inventario')),
            ],
        ),
    ]