from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.Crear_Tercero, name= 'Crear_Tercero'),
    path('listar/', views.Listar_Terceros, name='Listar_Terceros'),
    path('lista/<int:TERCEROS_id>/', views.Tercero_Creado, name='Tercero_Creado'),
    path('elimina/<int:TERCEROS_id>/', views.Eliminar_Tercero, name='Eliminar_Tercero'),
]