# Generated by Django 4.1.3 on 2022-11-13 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_usuarios", "0003_formacion"),
    ]

    operations = [
        migrations.RemoveField(model_name="formacion", name="curso",),
    ]
