from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating tasks.
    
    This demonstrates:
    - ModelForm usage
    - Form customization
    - Widget customization
    - Validation
    """
    
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description...',
                'maxlength': '200',
                'required': True,
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
        labels = {
            'title': 'Task Description',
            'completed': 'Mark as completed',
        }
        help_texts = {
            'title': 'Enter a clear description of what needs to be done.',
            'completed': 'Check this box if the task is already completed.',
        }
    
    def __init__(self, *args, **kwargs):
        """Customize form initialization."""
        super().__init__(*args, **kwargs)
        
        # Make title field required
        self.fields['title'].required = True
        
        # Add CSS classes for styling
        self.fields['title'].widget.attrs.update({
            'class': 'form-control task-input',
            'autofocus': True,
        })
        
        self.fields['completed'].widget.attrs.update({
            'class': 'form-check-input',
        })
    
    def clean_title(self):
        """Custom validation for title field."""
        title = self.cleaned_data.get('title')
        
        if title:
            # Remove extra whitespace
            title = title.strip()
            
            # Check minimum length
            if len(title) < 3:
                raise forms.ValidationError('Task title must be at least 3 characters long.')
            
            # Check for duplicate tasks (case-insensitive)
            existing_tasks = Task.objects.filter(title__iexact=title)
            if self.instance.pk:  # If updating, exclude current instance
                existing_tasks = existing_tasks.exclude(pk=self.instance.pk)
            
            if existing_tasks.exists():
                raise forms.ValidationError('A task with this title already exists.')
        
        return title
