# Generated by Django 4.2.4 on 2024-01-07 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0007_creditos_cap_ini'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='detalle_prod',
            unique_together={('hecho_econo', 'producto', 'subcuenta', 'concepto')},
        ),
    ]
