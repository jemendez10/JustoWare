# Generated by Django 5.0 on 2023-12-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imp_con_cre',
            name='descripcion',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
