from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .forms import TaskForm
from .models import todo_list


def index(request):
    tasks = todo_list.objects.all()
    title = "All tasks"
    return render(request, 'todo_list.html', {'tasks': tasks, 'title2': title})

def incomplete_tasks(request):
    tasks = todo_list.objects.filter(is_done=False)
    title = "Incompleted tasks"
    return render(request, 'todo_list.html', {'tasks': tasks, 'title2': title})
def add_task(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'save':
            f = TaskForm(request.POST)
            if f.is_valid():
                f.save()
                return redirect('index')
        if action == 'cancel':
            return redirect('index')
    else:
        f = TaskForm()
    return render(request, 'add_task.html', {'f': f})

def completed_task(request, task_id):
    t = todo_list.objects.get(id=task_id)
    t.is_done = not t.is_done
    t.save()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(todo_list, id=task_id)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'save':
            f = TaskForm(request.POST, instance=task)
            if f.is_valid():
                f.save()
                return redirect('index')
        if action == 'delete':
            task.delete()
            return redirect('index')
    else:
        f = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'f': f, 'task': task})
