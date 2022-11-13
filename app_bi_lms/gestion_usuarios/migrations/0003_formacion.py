# Generated by Django 4.1.3 on 2022-11-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_usuarios", "0002_curso"),
    ]

    operations = [
        migrations.CreateModel(
            name="Formacion",
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
                ("fecha_matricula_curso", models.DateField()),
                ("fecha_inicio_curso", models.DateField()),
                ("fecha_finalizacion_curso", models.DateField()),
                ("estado_curso", models.CharField(max_length=20)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion_usuarios.curso",
                    ),
                ),
                (
                    "gestor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion_usuarios.empleado",
                    ),
                ),
            ],
        ),
    ]
