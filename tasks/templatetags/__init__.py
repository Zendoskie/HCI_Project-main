from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def highlight(value):
    """
    Custom template filter to highlight important text.
    
    Wraps text in <strong> tags with yellow color styling.
    
    Usage in templates:
    {{ "Important text"|highlight }}
    """
    if not value:
        return value
    
    # Convert to string if it's not already
    text = str(value)
    
    # Wrap in strong tags with yellow color
    highlighted = f'<strong style="color: #ffff00;">{text}</strong>'
    
    # Return as safe HTML
    return mark_safe(highlighted)


@register.filter
def status_icon(value):
    """
    Custom template filter to show status icons.
    
    Returns ✅ for True, ❌ for False.
    
    Usage in templates:
    {{ task.completed|status_icon }}
    """
    if value is True:
        return mark_safe('✅')
    elif value is False:
        return mark_safe('❌')
    else:
        return value


@register.filter
def completion_percentage(completed_count, total_count):
    """
    Custom template filter to calculate completion percentage.
    
    Usage in templates:
    {{ completed_tasks|completion_percentage:total_tasks }}%
    """
    if total_count == 0:
        return 0
    
    percentage = (completed_count / total_count) * 100
    return round(percentage, 1)


@register.simple_tag
def get_task_stats():
    """
    Custom template tag to get task statistics.
    
    Usage in templates:
    {% get_task_stats as stats %}
    """
    from tasks.models import Task
    
    tasks = Task.objects.all()
    return {
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'pending': tasks.filter(completed=False).count(),
    }
