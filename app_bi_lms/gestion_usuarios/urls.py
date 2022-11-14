from django.urls import path
from gestion_usuarios import views

urlpatterns = [
    path("", views.login, name="Login"),
    path("home", views.home, name="Home"),
    path("formacion", views.formacion, name="Formacion"),
    path("mensajeria", views.mensajeria, name="Mensajeria"),
    path("mi_actividad", views.mi_actividad, name="Actividad"),
]
