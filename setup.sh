#!/bin/bash

# Django MVT Demo Setup Script
# This script sets up the Django project with sample data

echo "🚀 Setting up Django MVT Demo..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ Python and pip are available"

# Install requirements
echo "📦 Installing requirements..."
pip3 install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Create sample data
echo "📝 Creating sample data..."
python3 manage.py shell << EOF
from tasks.models import Task

# Clear existing tasks
Task.objects.all().delete()

# Create sample tasks
Task.objects.create(title="Learn Django MVT Architecture", completed=True)
Task.objects.create(title="Build a To-Do List App", completed=False)
Task.objects.create(title="Master Template Inheritance", completed=True)
Task.objects.create(title="Understand Context Processors", completed=False)
Task.objects.create(title="Create Custom Template Filters", completed=True)
Task.objects.create(title="Style with CSS and Static Files", completed=False)
Task.objects.create(title="Deploy to Production", completed=False)
Task.objects.create(title="Write Unit Tests", completed=False)

print("✅ Sample tasks created successfully!")
EOF

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Run the development server: python3 manage.py runserver"
echo "2. Open your browser to: http://127.0.0.1:8000/"
echo "3. Visit the admin interface: http://127.0.0.1:8000/admin/"
echo ""
echo "🔑 To create an admin user, run: python3 manage.py createsuperuser"
echo ""
echo "📚 Check the README.md file for detailed documentation"
