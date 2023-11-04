from django.shortcuts import render
from django.http import HttpResponse

import csv


# Create your views here.
def migracion(request):
    with open('c:/ajusto/Terceros.csv', 'r') as file:
        csv_reader = csv.DictReader(file,delimiter=';')
        for row in csv_reader:    
            print(row['NIT'])
    return HttpResponse("")