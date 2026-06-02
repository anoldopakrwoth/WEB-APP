from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile


class Command(BaseCommand):
    help = 'Create admin user with username and password "admin"'

    def handle(self, *args, **options):
        try:
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@agrilink.local',
                    'first_name': 'Admin',
                    'last_name': 'User',
                    'is_staff': True,
                    'is_superuser': True,
                },
            )

            admin_user.email = 'admin@agrilink.local'
            admin_user.first_name = 'Admin'
            admin_user.last_name = 'User'
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.set_password('admin')
            admin_user.save()

            UserProfile.objects.update_or_create(
                user=admin_user,
                defaults={
                    'role': 'admin',
                    'village': 'System',
                    'is_verified': True,
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS('Successfully created admin user'))
            else:
                self.stdout.write(self.style.SUCCESS('Successfully updated admin user'))
            self.stdout.write(self.style.SUCCESS('Username: admin'))
            self.stdout.write(self.style.SUCCESS('Password: admin'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {str(e)}'))
