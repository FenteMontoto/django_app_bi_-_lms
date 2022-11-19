# Generated by Django 4.1.3 on 2022-11-19 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "gestion_usuarios",
            "0013_alter_curso_cod_curso_alter_curso_nombre_curso_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Correo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gestor_envio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion_usuarios.empleado",
                    ),
                ),
            ],
        ),
    ]
