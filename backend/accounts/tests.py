from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import UserProfile


def load_setup_module():
    setup_path = Path(__file__).resolve().parents[1] / 'setup.py'
    spec = spec_from_file_location('agrilink_setup', setup_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SetupScriptTests(TestCase):
    def test_create_admin_user_is_idempotent(self):
        setup = load_setup_module()

        setup.create_admin_user()
        setup.create_admin_user()

        admin_user = User.objects.get(username='admin')
        self.assertEqual(User.objects.filter(username='admin').count(), 1)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.check_password('admin'))
        self.assertEqual(admin_user.profile.role, 'admin')

    def test_create_sample_users_is_idempotent(self):
        setup = load_setup_module()

        setup.create_sample_users()
        setup.create_sample_users()

        self.assertEqual(User.objects.filter(username='farmer1').count(), 1)
        self.assertEqual(User.objects.filter(username='buyer1').count(), 1)
        self.assertEqual(User.objects.get(username='farmer1').profile.role, 'farmer')
        self.assertEqual(User.objects.get(username='buyer1').profile.role, 'buyer')


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            password='Password123',
        )

    def test_logout_requires_post(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 405)

    def test_logout_post_redirects_to_login(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='profile-user',
            email='profile@example.com',
            first_name='Old',
            last_name='Name',
            password='Password123',
        )
        self.profile = self.user.profile
        self.profile.phone = '+256701111111'
        self.profile.village = 'Kampala'
        self.profile.address = 'Old address'
        self.profile.save()

    def test_profile_update_can_clear_optional_fields(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('profile'),
            {
                'first_name': '',
                'last_name': '',
                'email': self.user.email,
                'phone': '',
                'village': '',
                'address': '',
            },
        )

        self.assertRedirects(response, reverse('profile'))
        self.profile.refresh_from_db()
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
        self.assertEqual(self.profile.phone, '')
        self.assertEqual(self.profile.village, '')
        self.assertEqual(self.profile.address, '')
