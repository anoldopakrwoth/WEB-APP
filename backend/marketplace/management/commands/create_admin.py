from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile


class Command(BaseCommand):
    help = 'Create admin user with username and password "admin"'

    def handle(self, *args, **options):
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('Admin user already exists'))
            return

        try:
            # Create admin user
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@agrilink.local',
                password='admin',
                first_name='Admin',
                last_name='User'
            )

            # Create user profile for admin
            UserProfile.objects.create(
                user=admin_user,
                role='admin',
                village='System',
                is_verified=True
            )

            self.stdout.write(self.style.SUCCESS('Successfully created admin user'))
            self.stdout.write(self.style.SUCCESS('Username: admin'))
            self.stdout.write(self.style.SUCCESS('Password: admin'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {str(e)}'))
