# Generated by Django 4.1.3 on 2022-11-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_usuarios", "0004_remove_formacion_curso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="cod_empleado",
            field=models.CharField(
                max_length=6, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
