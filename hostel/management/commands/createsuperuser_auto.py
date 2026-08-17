from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


User = get_user_model()


class Command(BaseCommand):

    help = "Create or update default superuser"

    def handle(self, *args, **kwargs):

        username = os.environ.get(
            "DJANGO_SUPERUSER_USERNAME"
        )

        email = os.environ.get(
            "DJANGO_SUPERUSER_EMAIL",
            ""
        )

        password = os.environ.get(
            "DJANGO_SUPERUSER_PASSWORD"
        )

        if not username or not password:

            self.stdout.write(
                self.style.ERROR(
                    "Superuser environment variables missing"
                )
            )

            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )

        # Always update credentials
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.set_password(password)

        user.save()

        if created:

            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser created successfully"
                )
            )

        else:

            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser password updated successfully"
                )
            )