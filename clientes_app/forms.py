from django.shortcuts import render
from django import forms
from .models import CLIENTES
from django import forms
class CrearForm(forms.ModelForm):
    
    class Meta:
        model = CLIENTES
        fields = ['codigo','doc_ide','dv','sigla','nombre','direccion','telefono','celular','ciudad','email','dominio','nit_ger','nom_ger','nit_con','nom_con','tp_con','nit_rev_fis','nom_rev_fis','tp_rev_fis','age_ret','ret_iva','aut_ret','logo','num_lic','lic_act','ini_lic','fin_lic']
        widgets = {
                    'codigo': forms.TextInput(attrs={'class': 'form-control'}),
                    'doc_ide': forms.NumberInput(attrs={'class': 'form-control'}),
                    'dv': forms.TextInput(attrs={'class': 'form-control'}),
                    'sigla': forms.TextInput(attrs={'class': 'form-control'}),
                    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                    'direccion': forms.TextInput(attrs={'class': 'form-control'}),
                    'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
                    'celular': forms.NumberInput(attrs={'class': 'form-control'}),
                    'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.TextInput(attrs={'class': 'form-control'}),
                    'dominio': forms.TextInput(attrs={'class': 'form-control'}),
                    'nit_ger': forms.NumberInput(attrs={'class': 'form-control'}),
                    'nom_ger': forms.TextInput(attrs={'class': 'form-control'}),
                    'nit_con': forms.NumberInput(attrs={'class': 'form-control'}),
                    'nom_con': forms.TextInput(attrs={'class': 'form-control'}),
                    'tp_con': forms.TextInput(attrs={'class': 'form-control'}),
                    'nit_rev_fis': forms.NumberInput(attrs={'class': 'form-control'}),
                    'nom_rev_fis': forms.TextInput(attrs={'class': 'form-control'}),
                    'tp_rev_fis': forms.TextInput(attrs={'class': 'form-control'}),
                    'age_ret':forms.Select(attrs={'class': 'form-select'}),
                    'ret_iva': forms.Select(attrs={'class': 'form-select'}),
                    'aut_ret': forms.Select(attrs={'class': 'form-select'}),
                    'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                    'num_lic': forms.TextInput(attrs={'class': 'form-control'}),
                    'lic_act': forms.Select(attrs={'class': 'form-select'}),
                    'ini_lic': forms.DateInput(attrs={'class': 'form-control'}),
                    'fin_lic': forms.DateInput(attrs={'class': 'form-control'})
                }