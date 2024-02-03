from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.Crear_Localidad, name= 'Crear_Localidad'),
    path('listar/', views.Listar_Localidades, name='Listar_Localidades'),
    path('lista/<int:LOCALIDADES_id>/', views.Localidad_Creada, name='Localidad_Creada'),
    path('elimina/<int:LOCALIDADES_id>/', views.Eliminar_Localidad, name='Eliminar_Localidad'),
]