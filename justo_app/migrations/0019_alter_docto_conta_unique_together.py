# Generated by Django 5.0 on 2023-12-24 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0018_docto_conta_codigo_alter_docto_conta_nom_cto'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='docto_conta',
            unique_together={('oficina', 'per_con', 'codigo')},
        ),
    ]
