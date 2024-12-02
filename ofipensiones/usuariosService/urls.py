from django.urls import path
from . import views

urlpatterns = [
    path('listar-usuarios/', views.get, name='listar_usuarios')
    ]