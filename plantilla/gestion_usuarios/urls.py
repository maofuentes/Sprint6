from django.urls import path
from . import views


urlpatterns = [
    path("registrar_usuario", views.registrar_usuario, name="registrar_usuario"),
    path("inicio_sesion", views.inicio_sesion, name="inicio_sesion"),
    path("salir_sesion", views.salir, name="salir"),
    path("home", views.home, name="home"),
    path("vista_usuarios", views.vista_usuarios, name="vista_usuarios")
]