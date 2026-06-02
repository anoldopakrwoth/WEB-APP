"""General helper functions used across the project."""

from django.contrib.auth.models import User


def is_admin_user(user: User) -> bool:
    """Return True when the user has staff or superuser access."""
    return user.is_authenticated and (user.is_staff or user.is_superuser)
