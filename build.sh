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
