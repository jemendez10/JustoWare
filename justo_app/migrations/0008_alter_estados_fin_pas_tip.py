# Generated by Django 4.2.4 on 2023-11-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0007_alter_estados_fin_pas_otr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estados_fin',
            name='pas_tip',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
