from django.shortcuts import render
from django import forms
from .models import CLIENTES
from django import forms
class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CLIENTES
        fields = ['codigo','doc_ide','dv','sigla','nombre','direccion','telefono','celular','ciudad','email','dominio','nit_ger','nom_ger','nit_con','nom_con','tp_con','nit_rev_fis','nom_rev_fis','tp_rev_fis','age_ret','ret_iva','aut_ret','logo','num_lic','lic_act','ini_lic','fin_lic']
        widgets = {
                    'codigo': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'doc_ide': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'dv': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'sigla': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'nombre': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'direccion': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'telefono': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'celular': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'ciudad': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'email': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'dominio': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'nit_ger': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'nom_ger': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'nit_con': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'nom_con': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'tp_con': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'nit_rev_fis': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
                    'nom_rev_fis': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'tp_rev_fis': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'age_ret':forms.Select(attrs={'class': 'form-select rounded-pill'}),
                    'ret_iva': forms.Select(attrs={'class': 'form-select rounded-pill'}),
                    'aut_ret': forms.Select(attrs={'class': 'form-select rounded-pill'}),
                    'logo': forms.ClearableFileInput(attrs={'class': 'form-control rounded-pill'}),
                    'num_lic': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
                    'lic_act': forms.Select(attrs={'class': 'form-select rounded-pill'}),
                    'ini_lic': forms.DateInput(attrs={'class': 'form-control rounded-pill'}),
                    'fin_lic': forms.DateInput(attrs={'class': 'form-control rounded-pill'})
                }