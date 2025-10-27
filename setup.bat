@echo off
REM Django MVT Demo Setup Script for Windows
REM This script sets up the Django project with sample data

echo 🚀 Setting up Django MVT Demo...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python is available

REM Install requirements
echo 📦 Installing requirements...
pip install -r requirements.txt

REM Run migrations
echo 🗄️ Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Create sample data
echo 📝 Creating sample data...
python manage.py shell -c "
from tasks.models import Task
Task.objects.all().delete()
Task.objects.create(title='Learn Django MVT Architecture', completed=True)
Task.objects.create(title='Build a To-Do List App', completed=False)
Task.objects.create(title='Master Template Inheritance', completed=True)
Task.objects.create(title='Understand Context Processors', completed=False)
Task.objects.create(title='Create Custom Template Filters', completed=True)
Task.objects.create(title='Style with CSS and Static Files', completed=False)
Task.objects.create(title='Deploy to Production', completed=False)
Task.objects.create(title='Write Unit Tests', completed=False)
print('✅ Sample tasks created successfully!')
"

echo.
echo 🎉 Setup complete!
echo.
echo 📋 Next steps:
echo 1. Run the development server: python manage.py runserver
echo 2. Open your browser to: http://127.0.0.1:8000/
echo 3. Visit the admin interface: http://127.0.0.1:8000/admin/
echo.
echo 🔑 To create an admin user, run: python manage.py createsuperuser
echo.
echo 📚 Check the README.md file for detailed documentation
pause
