# Generated by Django 4.2.4 on 2024-01-07 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0008_alter_detalle_prod_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_prod',
            name='oficina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='justo_app.oficinas'),
        ),
    ]
