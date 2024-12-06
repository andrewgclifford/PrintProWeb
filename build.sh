#!/usr/bin/env bash
# exit on error
set -o errexit

# Install python dependencies
pip install -r requirements.txt

# Create migrations for each app
python manage.py makemigrations accounts
python manage.py makemigrations jobs

# Run migrations
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate accounts
python manage.py migrate jobs
python manage.py migrate

# Create superuser
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', 
                                '$DJANGO_SUPERUSER_EMAIL',
                                '$DJANGO_SUPERUSER_PASSWORD',
                                user_type='admin')
EOF
