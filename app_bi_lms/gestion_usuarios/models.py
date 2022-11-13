from django.db import models

# Create your models here.

class Empleado(models.Model):
    cod_empleado=models.CharField(max_length=6, primary_key="True", unique="True")
    nombre=models.CharField(max_length=30)
    primer=models.CharField(max_length=30)
    segundo=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    extension=models.IntegerField()
    fecha_nacimiento=models.DateField()
    fecha_incorporacion=models.DateField()
    discapacidad=models.CharField(max_length=2)
    reduccion_jornada=models.CharField(max_length=2)
    horas_jornada=models.IntegerField()
 

class Curso(models.Model):
    cod_curso=models.CharField(max_length=6)
    nombre_curso=models.CharField(max_length=70, primary_key="True", unique="True")
    tipo_curso=models.CharField(max_length=20)
    
class Formacion(models.Model):
    gestor=models.ForeignKey(Empleado,on_delete=models.CASCADE,)
    fecha_matricula_curso=models.DateField()
    fecha_inicio_curso=models.DateField()
    fecha_finalizacion_curso=models.DateField()
    estado_curso=models.CharField(max_length=20)