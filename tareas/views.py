from django.shortcuts import render, redirect
from .models import Tareas
from .form import TareaForm


# Crear y listar 

def crear(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = TareaForm()
    return render(request,'crear.html',{'form':form})

def listar(request):
    tareas = Tareas.objects.all()
    return render(request,'listar.html',{'tareas':tareas})

