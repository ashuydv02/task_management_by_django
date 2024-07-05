from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.models import Task
from .form import TaskForm
from datetime import datetime

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def createTask(request):
    if request.method == 'POST':
        data = request.POST
        task = Task(title=data['title'], description=data['description'],status=data['status'],due_date=data['due_date'])
        task.save()
        return redirect('home')
    return render(request, 'tasks/addTask.html')

def edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'tasks/editTask.html', {'task': task, 'form': form})
    return render(request, 'tasks/editTask.html', {'task': task})

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

