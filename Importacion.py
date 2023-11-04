import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')

# Initialize django application
import django
django.setup()

# Do what you want to debug and set breakpoints
import csv
from django.shortcuts import render
from django.http import HttpResponse
import justo_app.models as justoAppModels

def init():
    Cliente = justoAppModels.CLIENTES.objects.filter(codigo='A').first()
    with open('c:/ajusto/localidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            justoAppModels.LOCALIDADES.objects.create(cliente=Cliente,codigo=row['CODIGO'],
                nombre=row['NOMBRE'],cod_pos=row['CODPOS'],departamento=row['DPTO'])

init()