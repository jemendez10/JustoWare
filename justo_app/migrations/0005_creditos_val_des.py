# Generated by Django 4.2.4 on 2024-01-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0004_detalle_econo_detalle_eco_hecho_e_534ad7_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditos',
            name='val_des',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
