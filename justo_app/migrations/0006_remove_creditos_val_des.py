# Generated by Django 4.2.4 on 2024-01-05 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justo_app', '0005_creditos_val_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditos',
            name='val_des',
        ),
    ]
