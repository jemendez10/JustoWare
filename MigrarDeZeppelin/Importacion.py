# Here you should use all the logic that you have 
# in manage.py before execute_from_command_line(sys.argv)
# Generally there is only settings module set up:
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
    with open('c:/ajusto/localidades.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            #tercero = justoAppModels.TERCEROS.objects.filter(doc_ide=row['NIT'])
            # justoAppModels.TERCEROS.objects.create(
            print(row)

init()