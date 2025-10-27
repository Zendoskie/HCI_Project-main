# Django MVT Architecture Demo - To-Do List App

A comprehensive Django mini-project that demonstrates Django's MVT (Model-View-Template) architecture with advanced features including static files, custom template filters, and context processors.

## 🎯 Project Overview

This project showcases:
- **Models**: Task model with proper field definitions
- **Views**: Both function-based and class-based views
- **Templates**: Template inheritance, blocks, and custom filters
- **Static Files**: CSS styling with dark theme
- **Custom Template Filters**: Text highlighting and status icons
- **Context Processors**: Global template context
- **URL Patterns**: Dynamic routing with multiple endpoints

## 📁 Project Structure

```
todo_mvt_demo/
├── manage.py
├── requirements.txt
├── README.md
├── todo_mvt_demo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── task_extras.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── templates/
│   ├── base.html
│   └── tasks/
│       ├── task_list.html
│       └── task_list_cbv.html
└── static/
    └── css/
        └── style.css
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   # If you have git
   git clone <repository-url>
   cd todo_mvt_demo
   
   # Or extract the downloaded files
   cd /path/to/todo_mvt_demo
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin interface: `http://127.0.0.1:8000/admin/`

## 📊 Adding Sample Data

### Method 1: Django Admin Interface
1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Click on "Tasks" under the "TASK MANAGEMENT" section
4. Click "Add Task" and create some sample tasks

### Method 2: Django Shell
```bash
python manage.py shell
```

```python
from tasks.models import Task

# Create sample tasks
Task.objects.create(title="Learn Django MVT Architecture", completed=True)
Task.objects.create(title="Build a To-Do List App", completed=False)
Task.objects.create(title="Master Template Inheritance", completed=True)
Task.objects.create(title="Understand Context Processors", completed=False)
Task.objects.create(title="Create Custom Template Filters", completed=True)
Task.objects.create(title="Style with CSS and Static Files", completed=False)

# Exit shell
exit()
```

## 🌐 Available URLs

| URL | View Type | Description |
|-----|-----------|-------------|
| `/` | Function-based | Main task list with add/edit/delete functionality |
| `/cbv/` | Class-based | Task list using Django's ListView with full CRUD |
| `/toggle/<id>/` | Function-based | Toggle task completion status |
| `/delete/<id>/` | Function-based | Delete a task |
| `/edit/<id>/` | Class-based | Edit task using UpdateView |
| `/delete-cbv/<id>/` | Class-based | Delete task using DeleteView |
| `/api/stats/` | API endpoint | JSON response with task statistics |
| `/admin/` | Admin interface | Django admin for managing tasks |

## 🎨 Features Demonstrated

### 1. Models
- **Task Model**: Fields include `title`, `completed`, and `created_at`
- **Model Methods**: `__str__()` and `toggle_completion()`
- **Meta Options**: Ordering and verbose names

### 2. Views
- **Function-based View**: `task_list()` with manual context creation and form handling
- **Class-based View**: `TaskListView` using Django's `ListView` with POST handling
- **Interactive Views**: `toggle_task()`, `delete_task()` for task management
- **CRUD Views**: `TaskUpdateView`, `TaskDeleteView` using generic views
- **API View**: `task_stats_api()` returning JSON data

### 3. Templates
- **Template Inheritance**: `base.html` with blocks and message handling
- **Interactive Templates**: Forms for adding, editing, and deleting tasks
- **Template Tags**: `{% for %}`, `{% if %}`, `{% load %}`, `{% csrf_token %}`
- **Template Filters**: `|upper`, `|date`, `|yesno`, `|truncatechars`
- **Custom Filters**: `|highlight` for text highlighting

### 4. Forms
- **ModelForm**: `TaskForm` for creating and updating tasks
- **Form Validation**: Custom validation for title length and duplicates
- **Form Handling**: Both function-based and class-based form processing
- **Error Handling**: Display form errors with user feedback

### 5. Static Files
- **CSS Styling**: Dark theme with responsive design
- **Static File Loading**: `{% load static %}` and `{% static %}` tags
- **Modern UI**: Cards, grids, animations, and interactive buttons
- **Form Styling**: Beautiful form layouts with validation feedback

### 6. Custom Template Filters
- **highlight**: Wraps text in yellow `<strong>` tags
- **status_icon**: Shows ✅ or ❌ based on boolean value
- **completion_percentage**: Calculates completion percentage

### 7. Context Processors
- **Global Context**: App name available in all templates
- **Additional Data**: App version and description

### 8. Interactive Features
- **Add Tasks**: Create new tasks with form validation
- **Toggle Completion**: Mark tasks as complete/incomplete
- **Edit Tasks**: Update task details with pre-filled forms
- **Delete Tasks**: Remove tasks with confirmation dialogs
- **Real-time Feedback**: Success/error messages for all actions

## 🔧 Key Django Concepts Demonstrated

### MVT Architecture
- **Model**: `Task` model with database fields
- **View**: Function-based and class-based views
- **Template**: HTML templates with Django template language

### URL Patterns
- Dynamic URL routing
- Namespace usage (`tasks:`)
- Multiple URL patterns

### Template System
- Template inheritance with blocks
- Template tags and filters
- Custom template filters and tags

### Static Files
- CSS file organization
- Static file serving in development
- Template integration

### Admin Interface
- Model registration
- Custom admin configuration
- List display and filtering

## 🧪 Testing the Application

1. **Visit the main page** (`http://127.0.0.1:8000/`)
   - See function-based view in action
   - Check template inheritance
   - Verify custom filters work

2. **Visit the class-based view** (`http://127.0.0.1:8000/cbv/`)
   - Compare with function-based view
   - See same data, different implementation

3. **Check the API endpoint** (`http://127.0.0.1:8000/api/stats/`)
   - View JSON response
   - See task statistics

4. **Add tasks via admin** (`http://127.0.0.1:8000/admin/`)
   - Create new tasks
   - Mark tasks as completed
   - See changes reflected on main pages

## 🎓 Learning Objectives Achieved

This project demonstrates:

✅ **Function-based vs Class-based views**
- Both approaches to handling HTTP requests
- When to use each type

✅ **Template rendering and context**
- Passing data from views to templates
- Context enhancement in class-based views

✅ **Template inheritance and blocks**
- DRY principle in templates
- Reusable base templates

✅ **URL patterns with dynamic paths**
- URL routing and namespacing
- Multiple endpoints

✅ **Static files (CSS, JS, Images)**
- Organizing static assets
- Template integration

✅ **Template filters and custom tags**
- Built-in Django filters
- Creating custom filters

✅ **Building a simple mini-project**
- Complete Django application
- Real-world project structure

✅ **Context processors**
- Global template context
- Application-wide data

## 🚀 Next Steps

To extend this project, consider adding:

1. **User Authentication**
   - User registration and login
   - User-specific tasks

2. **CRUD Operations**
   - Add, edit, delete tasks
   - Form handling

3. **AJAX Functionality**
   - Dynamic task updates
   - Real-time statistics

4. **Additional Features**
   - Task categories
   - Due dates
   - Task priorities

5. **Testing**
   - Unit tests for models
   - Integration tests for views

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Template Language](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Django Class-Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

---

**Happy Coding! 🎉**