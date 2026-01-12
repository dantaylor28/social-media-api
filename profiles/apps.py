# profiles/apps.py
from django.apps import AppConfig
import os

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def ready(self):
        from django.contrib.auth import get_user_model

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            return

        User = get_user_model()

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            print("✅ Superuser created")
