# Generated by Django 4.2.4 on 2023-11-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0014_originacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originacion',
            name='fec_sol',
            field=models.DateField(blank=True),
        ),
    ]
