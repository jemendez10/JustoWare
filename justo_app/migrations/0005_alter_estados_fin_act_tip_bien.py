# Generated by Django 4.2.4 on 2023-11-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0004_alter_estados_fin_act_otr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estados_fin',
            name='act_tip_bien',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
