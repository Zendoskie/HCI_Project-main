from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    """
    Function-based view to display all tasks with add functionality.
    
    This demonstrates:
    - Function-based views
    - Template rendering with context
    - Querying the database
    - Form handling
    """
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    
    # Add some context data
    context = {
        'tasks': tasks,
        'total_tasks': tasks.count(),
        'completed_tasks': tasks.filter(completed=True).count(),
        'pending_tasks': tasks.filter(completed=False).count(),
        'view_type': 'Function-Based View',
        'form': form,
    }
    
    return render(request, 'tasks/task_list.html', context)


class TaskListView(ListView):
    """
    Class-based view to display all tasks with add functionality.
    
    This demonstrates:
    - Class-based views
    - Django's generic ListView
    - Automatic template rendering
    - Context data enhancement
    - Form handling in class-based views
    """
    model = Task
    template_name = 'tasks/task_list_cbv.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        """
        Add extra context data to the template.
        
        This method demonstrates how to enhance the context
        in class-based views.
        """
        context = super().get_context_data(**kwargs)
        tasks = context['tasks']
        
        context.update({
            'total_tasks': tasks.count(),
            'completed_tasks': tasks.filter(completed=True).count(),
            'pending_tasks': tasks.filter(completed=False).count(),
            'view_type': 'Class-Based View (ListView)',
            'form': TaskForm(),
        })
        
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle POST requests for adding new tasks."""
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('tasks:task_list_cbv')
        else:
            # If form is invalid, re-render the page with errors
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


def task_stats_api(request):
    """
    API endpoint to get task statistics.
    
    This demonstrates:
    - JSON responses
    - API endpoints
    - Data aggregation
    """
    tasks = Task.objects.all()
    
    stats = {
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'pending': tasks.filter(completed=False).count(),
        'completion_rate': round(
            (tasks.filter(completed=True).count() / tasks.count() * 100) 
            if tasks.count() > 0 else 0, 2
        )
    }
    
    return JsonResponse(stats)


def stats_page(request):
    """
    Display statistics in a nice HTML page.
    
    This demonstrates:
    - HTML page for API data
    - Better visualization of statistics
    - User-friendly interface
    """
    tasks = Task.objects.all()
    
    # Calculate statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()
    completion_rate = round(
        (completed_tasks / total_tasks * 100) 
        if total_tasks > 0 else 0, 1
    )
    
    # Get recent tasks
    recent_tasks = tasks.order_by('-created_at')[:5]
    
    # Get completion trends (last 7 days)
    from django.utils import timezone
    from datetime import timedelta
    
    week_ago = timezone.now() - timedelta(days=7)
    recent_completed = tasks.filter(completed=True, created_at__gte=week_ago).count()
    recent_created = tasks.filter(created_at__gte=week_ago).count()
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_rate': completion_rate,
        'recent_tasks': recent_tasks,
        'recent_completed': recent_completed,
        'recent_created': recent_created,
        'view_type': 'Task Statistics Dashboard',
    }
    
    return render(request, 'tasks/stats_page.html', context)


@require_POST
def toggle_task(request, task_id):
    """
    Toggle task completion status.
    
    This demonstrates:
    - AJAX-style interactions
    - POST-only views
    - Task state management
    """
    task = get_object_or_404(Task, id=task_id)
    task.toggle_completion()
    
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'success': True,
            'completed': task.completed,
            'message': f'Task marked as {"completed" if task.completed else "pending"}'
        })
    
    messages.success(request, f'Task marked as {"completed" if task.completed else "pending"}!')
    return redirect(request.META.get('HTTP_REFERER', 'tasks:task_list'))


@require_POST
def delete_task(request, task_id):
    """
    Delete a task.
    
    This demonstrates:
    - Task deletion
    - Confirmation handling
    - Redirect after action
    """
    task = get_object_or_404(Task, id=task_id)
    task_title = task.title
    task.delete()
    
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'success': True,
            'message': f'Task "{task_title}" deleted successfully'
        })
    
    messages.success(request, f'Task "{task_title}" deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER', 'tasks:task_list'))


class TaskUpdateView(UpdateView):
    """
    Class-based view for updating tasks.
    
    This demonstrates:
    - UpdateView generic view
    - Form handling
    - Success URL redirection
    """
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')
    
    def get_success_url(self):
        """Redirect to the appropriate list view."""
        if 'cbv' in self.request.META.get('HTTP_REFERER', ''):
            return reverse_lazy('tasks:task_list_cbv')
        return reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    """
    Class-based view for deleting tasks.
    
    This demonstrates:
    - DeleteView generic view
    - Confirmation templates
    - Success URL redirection
    """
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')
    
    def get_success_url(self):
        """Redirect to the appropriate list view."""
        if 'cbv' in self.request.META.get('HTTP_REFERER', ''):
            return reverse_lazy('tasks:task_list_cbv')
        return reverse_lazy('tasks:task_list')
