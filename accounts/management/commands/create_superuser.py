from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser if one does not exist'

    def handle(self, *args, **kwargs):
        username = settings.DJANGO_SUPERUSER_USERNAME
        email = settings.DJANGO_SUPERUSER_EMAIL
        password = settings.DJANGO_SUPERUSER_PASSWORD

        try:
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} already exists'))
                return
                
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                user_type='admin'
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))
