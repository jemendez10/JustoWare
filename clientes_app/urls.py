from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.Crear_Cliente, name= 'Crear_Cliente'),
    path('listar/', views.Listar_Clientes, name='Listar_Clientes'),
    path('lista/<int:CLIENTES_id>/', views.Cliente_Creado, name='Cliente_Creado'),
    path('elimina/<int:CLIENTES_id>/', views.Eliminar_Cliente, name='Eliminar_Cliente'),
]