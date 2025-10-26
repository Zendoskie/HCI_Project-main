from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


def home(request):
    """Home page: list all tasks"""
    tasks = Task.objects.all()
    return render(request, 'tracker/home.html', {'tasks': tasks})


def add_task(request):
    """Add Task: form to add a new task"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title and description:
            Task.objects.create(title=title, description=description)
            messages.success(request, 'Task added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'tracker/add_task.html')


def update_task(request, task_id):
    """Update Task: mark as complete/incomplete"""
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    
    status = "completed" if task.completed else "marked as incomplete"
    messages.success(request, f'Task "{task.title}" {status}!')
    return redirect('home')


def delete_task(request, task_id):
    """Delete Task: remove a task"""
    task = get_object_or_404(Task, id=task_id)
    task_title = task.title
    task.delete()
    
    messages.success(request, f'Task "{task_title}" deleted successfully!')
    return redirect('home')
