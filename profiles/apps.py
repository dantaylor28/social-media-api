# profiles/apps.py
import os
from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    def ready(self):
        if os.environ.get("RESET_SUPERUSER") == "true":
            from django.contrib.auth import get_user_model

            User = get_user_model()
            username = os.environ.get("SUPERUSER_USERNAME")
            password = os.environ.get("SUPERUSER_PASSWORD")

            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                print(f"✅ Superuser '{username}' password reset")
            except User.DoesNotExist:
                print(f"❌ Superuser '{username}' not found")
