from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def base(request):
    return render(request, 'base.html')  


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html')

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasktracker/task_detail.html', {'task': task})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasktracker/create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasktracker/edit_task.html', {'form': form, 'task': task})
