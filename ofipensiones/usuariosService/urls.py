from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/listar-usuarios/', views.get, name='listar_usuarios')
    ]