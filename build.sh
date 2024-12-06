#!/usr/bin/env bash
# exit on error
set -o errexit

# Install python dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate
