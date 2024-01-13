from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CrearForm
from .models import CLIENTES

@login_required
def Crear_Cliente(request):
    if request.method == 'GET':
        return render(request, 'Crear_Cliente.html', {'form': CrearForm})
    else:
        try:
            form = CrearForm(request.POST)
            new = form.save(commit = False)
            new.save()
            return render(request, 'Crear_Cliente.html',{'form': CrearForm})
        except ValueError:
            return render(request, 'Crear_Cliente.html', {
                'form': CrearForm,
                'error':'Los valores ingresados ya existen o no son válidos'
                })


@login_required
def Listar_Clientes(request):
    Lista = CLIENTES.objects.all()
    return render(request, 'Listar_Clientes.html', {'Lista': Lista})

class Lista_Clientes(ListView):
    model = CLIENTES
    template_name = 'Listar_Clientes.html'


@login_required
def Cliente_Creado(request, CLIENTES_id):
    if request.method == 'GET':
        Clientes = get_object_or_404(CLIENTES, pk = CLIENTES_id)
        form = CrearForm(instance=Clientes)
        return render(request, 'Cliente_Creado.hmtl',{'Clientes': Clientes, 'form':form})
    else:
        try:
            cliente = get_object_or_404(CLIENTES, pk = CLIENTES_id)
            form = CrearForm(request.POST, instance = cliente)
            form.save()
            return redirect('Listar_Clientes')
        except ValueError:
            return render(request, 'Cliente_Creado.html',{'Clientes': cliente, 'form': form,'error':'Error al actualizar'})
        

@login_required
def Eliminar_Cliente(request, CLIENTES_id):
    Cliente = get_object_or_404(CLIENTES, pk=CLIENTES_id)
    if request.method == 'POST':
        Cliente.delete()
        return redirect('Listar_Clientes')
