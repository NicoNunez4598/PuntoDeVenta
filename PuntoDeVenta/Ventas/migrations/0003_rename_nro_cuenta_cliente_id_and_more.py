# Generated by Django 5.2 on 2025-04-20 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_cliente_impositivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nro_cuenta',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nro_producto',
            new_name='id',
        ),
    ]
