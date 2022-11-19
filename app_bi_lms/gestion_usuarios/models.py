from django.db import models

# Create your models here.

class Empleado(models.Model):
    
    cod_empleado=models.CharField(max_length=6, primary_key=True, unique=True)
    nombre=models.CharField(max_length=30)
    primer=models.CharField(max_length=30, verbose_name="Primer apellido")
    segundo=models.CharField(max_length=30, verbose_name="Segundo apellido")
    email=models.EmailField(blank=True, null=True)
    extension=models.IntegerField()
    departamento=models.CharField(max_length=30,blank=True, null=True)
    delegacion=models.CharField(max_length=30,blank=True, null=True)
    grupo_titular=models.CharField(max_length=30,blank=True, null=True)
    servicio_titular=models.CharField(max_length=30,blank=True, null=True)
    grupo_refuerzo=models.CharField(max_length=30,blank=True, null=True)
    servicio_refuerzo_1=models.CharField(max_length=30,blank=True, null=True)
    servicio_refuerzo_2=models.CharField(max_length=30,blank=True, null=True)
    fecha_nacimiento=models.DateField()
    fecha_incorporacion=models.DateField()
    discapacidad=models.CharField(max_length=2)
    reduccion_jornada=models.CharField(max_length=2)
    horas_jornada=models.IntegerField()
    
    def __str__(self):
        return self.cod_empleado
 

class Curso(models.Model):
    cod_curso=models.CharField(max_length=6,verbose_name="Código curso")
    nombre_curso=models.CharField(max_length=70,verbose_name="Nombre del curso", primary_key="True", unique="True")
    tipo_curso=models.CharField(max_length=20,verbose_name="Tipo de curso")
    def __str__(self):
        return self.nombre_curso
    
class Formacion(models.Model):
    gestor=models.ForeignKey(Empleado,on_delete=models.CASCADE,)
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE,)
    fecha_matricula_curso=models.DateField()
    fecha_inicio_curso=models.DateField()
    fecha_finalizacion_curso=models.DateField()
    estado_curso=models.CharField(max_length=20,verbose_name="Estado")
    

 
    