from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser with the specified username and password'

    def handle(self, *args, **options):
        username = getattr(settings, 'DJANGO_SUPERUSER_USERNAME', 'admin')
        email = getattr(settings, 'DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = getattr(settings, 'DJANGO_SUPERUSER_PASSWORD', 'admin123')

        if not username:
            self.stdout.write(self.style.ERROR('Username must be set'))
            return

        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                    user_type='admin'
                )
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists'))
