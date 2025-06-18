#!/bin/bash

echo "Running makemigrations..."
python manage.py makemigrations

echo "Running migrate..."
python manage.py migrate

echo "Creating superuser if it doesn't exist..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', '834000')
EOF

echo "Starting Gunicorn..."
exec gunicorn lms_project.wsgi:application --bind 0.0.0.0:8000