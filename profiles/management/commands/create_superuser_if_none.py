# profiles/management/commands/create_superuser_if_none.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Create a superuser if none exists"

    def handle(self, *args, **options):
        if os.getenv("CREATE_SUPERUSER") != "true":
            return

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("Superuser already exists")
            return

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not all([username, email, password]):
            self.stdout.write("Missing env vars")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write("✅ Superuser created")
