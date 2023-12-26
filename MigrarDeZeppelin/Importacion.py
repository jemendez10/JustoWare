# Here you should use all the logic that you have 
# in manage.py before execute_from_command_line(sys.argv)
# Generally there is only settings module set up:

# Initialize django application
import django
django.setup()

# Do what you want to debug and set breakpoints
import csv
from django.shortcuts import render
from django.http import HttpResponse
from justo_app.models import TERCEROS

def init():
    with open('c:/ajusto/Terceros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:
            #   tercero = justoAppModels.TERCEROS.objects.filter(doc_ide=row['NIT'])
            #   justoAppModels.TERCEROS.objects.create(
            print(row)

init()