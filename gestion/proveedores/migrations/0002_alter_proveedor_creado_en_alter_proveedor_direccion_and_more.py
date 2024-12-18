# Generated by Django 5.1.4 on 2024-12-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='creado_en',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_razon_social',
            field=models.CharField(max_length=100, verbose_name='Nombre o Razón Social'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='notas',
            field=models.TextField(blank=True, null=True, verbose_name='Notas o Comentarios'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.CharField(help_text='Debe ingresar el RUT en el formato 12345678-9', max_length=12, unique=True, verbose_name='RUT'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, help_text='Ingrese el teléfono en formato internacional, por ejemplo: +56 9 1234 5678', max_length=15, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='tipo_proveedor',
            field=models.CharField(choices=[('Aseo', 'Aseo'), ('Despensa', 'Despensa'), ('Congelados', 'Congelados'), ('Cuidado Personal', 'Cuidado Personal')], default='Aseo', max_length=16, verbose_name='Tipo de Proveedor'),
        ),
    ]
