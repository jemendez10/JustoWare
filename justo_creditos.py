import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Justo_proy.settings')

# Initialize django application
import django
django.setup()

# Do what you want to debug and set breakpoints
import csv
from django.shortcuts import render
from django.http import HttpResponse
import justo_app.models as justo
from datetime import datetime
from django.db.models.query import QuerySet
from django.db.models import F, Sum, Case, When, Value, FloatField, CharField, IntegerField
from django.db.models.functions import Coalesce
from operator import itemgetter


def prueba():
    TIPOS_MOV_CRE = {
        'DESEM': '0',
        'CAUSA': '1',
        'AJUST': '2',
        'DESPP': '3',
        'KASCO': '4',
        'CASTI': '5',
        'CONDO': '6',
        'ABOCA': '7',
        'ABOCU': '8',
        'CUOTA': '9'
    }
    print('Duracion  ',datetime.now())
    Cliente = justo.CLIENTES.objects.filter(codigo='A').first()
    Oficina = justo.OFICINAS.objects.filter(codigo='A0001').first()
    Creditos = justo.CREDITOS.objects.filter(oficina=Oficina,estado = 'A',cod_cre = '133722')
    xTotSal = 0
    xNumCre = 0
    for Credito in Creditos:
        queryset1 = justo.CREDITOS_CAUSA.objects.values('fecha', 'cuota') \
            .filter(oficina=Oficina, cod_cre=Credito.cod_cre) \
            .annotate(
                tipmov=Value('1'),
            kapital=F('capital'),
            intcor=F('int_cor'),
            intmor=Value(0, output_field=IntegerField()),
            polseg=Value(0, output_field=IntegerField()),
            despp=Value(0, output_field=IntegerField()),
            acreed=Value(0, output_field=IntegerField())
        )

        #for lista in queryset1:
        #    print(lista)
        #    break
        queryset2 = justo.DETALLE_PROD.objects.filter(oficina=Oficina, producto='CR', subcuenta=Credito.cod_cre) \
            .values(fecha=F('hecho_econo__fecha')) \
            .annotate(
                cuota=Value(0),
                tipmov=Case(
                    *[When(concepto=concept, then=Value(value)) for concept, value in TIPOS_MOV_CRE.items()],
                    output_field=CharField()
                ),
                kapital=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Kapita', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                intcor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntCor', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                intmor=Coalesce(Sum(Case(When(detalle_econo__item_concepto='IntMor', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                polseg=Coalesce(Sum(Case(When(detalle_econo__item_concepto='PolSeg', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                despp=Coalesce(Sum(Case(When(detalle_econo__item_concepto='DesPP', then=-F('detalle_econo__valor_2')))), Value(0.0)),
                acreed=Coalesce(Sum(Case(When(detalle_econo__item_concepto='Acreed', then=-F('detalle_econo__valor_2')))), Value(0.0)) 
            )
        #for lista in queryset2:
        #    print(lista)
        #    break

        queryset3 = justo.CAMBIOS_CRE.objects.filter(det_pro__oficina=Oficina, det_pro__producto='CR', det_pro__subcuenta=Credito.cod_cre) \
            .values(fecha=F('det_pro__hecho_econo__fecha')) \
            .annotate(
                cuota=Value(0, output_field=IntegerField()),
                tipmov=F('tip_cam'),
                kapital=F('capital'),
                intcor=F('int_cor'),
                intmor=F('int_mor'),
                polseg=F('pol_seg'),
                despp=Value(0, output_field=IntegerField()),
                acreed=F('acreedor')
            )
        tab_liq = list(queryset1) + list(queryset2) + list(queryset3)
        tab_liq = sorted(tab_liq, key = itemgetter('fecha', 'tipmov'))
        nr = 0
        for objeto in tab_liq:
            print(objeto)
        saldo = sum(objeto['kapital'] for objeto in tab_liq if objeto['tipmov'] != '0')
        #print(Credito.cod_cre,' ', saldo)
        xTotSal = xTotSal + saldo
        xNumCre = xNumCre + 1
    print('Creditos  ',xNumCre,'   ',xTotSal)
    print('Fin       ',datetime.now())

def init():
    prueba()

init()