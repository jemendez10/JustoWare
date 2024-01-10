# Generated by Django 4.2.4 on 2024-01-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0010_detalle_prod_detalle_pro_oficina_aca602_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='detalle_prod',
            name='detalle_pro_oficina_aca602_idx',
        ),
        migrations.AddIndex(
            model_name='detalle_prod',
            index=models.Index(fields=['oficina', 'producto', 'subcuenta'], name='detalle_pro_oficina_9a63d9_idx'),
        ),
    ]
