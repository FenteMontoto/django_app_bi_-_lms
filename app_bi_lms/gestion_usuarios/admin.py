from django.contrib import admin
from gestion_usuarios.models import Empleado
from gestion_usuarios.models import Curso
from gestion_usuarios.models import Formacion
# Register your models here.

admin.site.register(Empleado)
admin.site.register(Curso)
admin.site.register(Formacion)