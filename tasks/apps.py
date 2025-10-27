from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    verbose_name = 'Task Management'
    
    def ready(self):
        """Called when the app is ready."""
        # Import signal handlers here if needed
        pass
