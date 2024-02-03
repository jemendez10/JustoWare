from django.shortcuts import render
from django import forms
from .models import LOCALIDADES

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = LOCALIDADES
        fields = ['codigo','nombre','cod_pos','departamento']
