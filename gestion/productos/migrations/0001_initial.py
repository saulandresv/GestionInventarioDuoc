# Generated by Django 5.1.4 on 2024-12-07 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('aseo', 'Aseo'), ('Despensa', 'Despensa'), ('Congelados', 'Congelados'), ('Cuidado Personal', 'Cuidado Personal')], default='aseo', max_length=16)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productos', to='proveedores.proveedor')),
            ],
        ),
    ]
