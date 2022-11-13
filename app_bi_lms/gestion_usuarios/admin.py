from django.contrib import admin
from gestion_usuarios.models import Empleado
from gestion_usuarios.models import Curso
from gestion_usuarios.models import Formacion
# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('cod_empleado','nombre','primer','segundo','departamento')
    search_fields=('cod_empleado','nombre','primer','segundo','departamento')
    list_filter=('departamento','discapacidad','reduccion_jornada',)
    
class CursoAdmin(admin.ModelAdmin):
    list_display=('cod_curso','nombre_curso')
    search_fields=('cod_curso','nombre_curso')
   
class FormacionAdmin(admin.ModelAdmin):
    list_display=('gestor','curso','fecha_inicio_curso','fecha_finalizacion_curso','estado_curso')
    search_fields=('gestor','curso','fecha_inicio_curso','fecha_finalizacion_curso','estado_curso')
    list_filter=('estado_curso','fecha_finalizacion_curso',)
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Formacion,FormacionAdmin)