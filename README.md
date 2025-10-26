# Task Tracker Demo - Django MVT Pattern

A Django web application demonstrating the Model-View-Template (MVT) pattern with a simple task management system.

## Features

- **Model**: Task model with title, description, completion status, and creation timestamp
- **Views**: CRUD operations for task management
- **Templates**: Clean, responsive HTML templates with CSS styling
- **Context Processor**: Global app name available in all templates

## Project Structure

```
tasktracker/
├── manage.py
├── requirements.txt
├── README.md
├── tasktracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tracker/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── templates/
│       └── tracker/
│           ├── base.html
│           ├── home.html
│           └── add_task.html
└── static/
    └── tracker/
        └── css/
            └── style.css
```

## Installation & Setup

1. **Install Django**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Development Server**:
   ```bash
  python3 manage.py runserver
   ```

5. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel available at `http://127.0.0.1:8000/admin/`

## URL Patterns

- `/` - Home page (list all tasks)
- `/add/` - Add new task form
- `/update/<int:id>/` - Toggle task completion status
- `/delete/<int:id>/` - Delete a task

## MVT Pattern Implementation

### Model (tracker/models.py)
- `Task` model with fields: title, description, completed, created_at
- String representation and ordering defined

### Views (tracker/views.py)
- `home()` - List all tasks
- `add_task()` - Handle task creation form
- `update_task()` - Toggle completion status
- `delete_task()` - Remove tasks

### Templates (tracker/templates/)
- `base.html` - Base template with navigation and styling
- `home.html` - Task list display with actions
- `add_task.html` - Task creation form

## Features Demonstrated

1. **Django MVT Architecture**: Clear separation of concerns
2. **Template Inheritance**: Base template extended by other templates
3. **Context Processors**: Global app name available in all templates
4. **Static Files**: CSS styling for responsive design
5. **Form Handling**: POST requests for task creation
6. **URL Routing**: Clean URL patterns with parameters
7. **Database Operations**: CRUD operations on Task model
8. **User Feedback**: Success/error messages
9. **Responsive Design**: Mobile-friendly CSS

## Styling Features

- Modern gradient header design
- Alternating row colors for task table
- Green highlighting for completed tasks
- Responsive design for mobile devices
- Hover effects and smooth transitions
- Clean form styling with focus states

## Command Line Demo Steps

```bash
# 1. Navigate to project directory
cd /path/to/tasktracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start the development server
python3 manage.py runserver

# 5. Open browser and visit
# http://127.0.0.1:8000/
```

## Admin Interface

Access the Django admin interface at `http://127.0.0.1:8000/admin/` to:
- View all tasks in a table format
- Edit task details directly
- Filter tasks by completion status
- Search tasks by title or description
- Bulk edit task completion status

This project demonstrates a complete Django MVT implementation with modern web development practices.
