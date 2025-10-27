from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Task model representing a todo item.
    
    Fields:
    - title: The task description
    - completed: Whether the task is completed
    - created_at: When the task was created
    """
    title = models.CharField(max_length=200, help_text="Enter the task description")
    completed = models.BooleanField(default=False, help_text="Mark as completed")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Task creation time")
    
    class Meta:
        ordering = ['-created_at']  # Most recent tasks first
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    def __str__(self):
        """String representation of the task."""
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title}"
    
    def toggle_completion(self):
        """Toggle the completion status of the task."""
        self.completed = not self.completed
        self.save()
