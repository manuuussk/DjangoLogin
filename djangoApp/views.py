from django.shortcuts import render, redirect
from djangoApp.models import Tarefas

def index(request):
    return render(request,'djangoApp/index.html')

def tasks(request):
    tarefas = Tarefas.objects.all()
    return render(request,'djangoApp/tasks.html', {'tarefas': tarefas})

def create_task(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao =request.POST.get('descricao')
        data = request.POST.get('data')
        status = FALSE

        Tarefa.objects.create(titulo=titulo,descricao=descricao,data=data)
        return redirect('tasks')
    return render(request, 'task/tasks.html')