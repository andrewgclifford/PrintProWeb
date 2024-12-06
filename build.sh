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
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123', user_type='admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell
