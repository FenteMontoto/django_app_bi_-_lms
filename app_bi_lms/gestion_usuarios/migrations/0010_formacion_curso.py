# Generated by Django 4.1.3 on 2022-11-13 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_usuarios", "0009_alter_empleado_grupo_titular_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="formacion",
            name="curso",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="gestion_usuarios.curso",
            ),
            preserve_default=False,
        ),
    ]
