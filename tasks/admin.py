from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Task model.
    
    This provides a nice interface in Django admin
    for managing tasks.
    """
    list_display = ['title', 'completed', 'created_at']
    list_filter = ['completed', 'created_at']
    search_fields = ['title']
    list_editable = ['completed']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at']
    
    def get_queryset(self, request):
        """Optimize queryset for admin list view."""
        return super().get_queryset(request).select_related()
