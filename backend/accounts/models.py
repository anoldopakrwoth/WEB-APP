"""
User account models for authentication and profiles.

This module defines user-related models including extended profile
information for farmers and buyers on the platform.
"""

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Extended user profile to store additional agricultural platform information.
    
    This model extends Django's User model with application-specific fields
    for farmers and buyers, including role information, location, and
    verification status.
    
    Attributes:
        user (OneToOneField): Reference to Django User model
        role (str): User role - 'farmer', 'buyer', or 'admin'
        phone (str): Contact phone number
        address (str): Physical address
        village (str): Village or town name
        profile_picture (ImageField): User avatar/profile photo
        is_verified (bool): Whether user email has been verified
        created_at (DateTime): Profile creation timestamp
        updated_at (DateTime): Last profile update timestamp
    """

    USER_ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
        ('admin', 'Administrator'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        help_text='Reference to Django user account'
    )
    
    role = models.CharField(
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default='buyer',
        help_text='User role on the platform'
    )
    
    phone = models.CharField(
        max_length=15,
        blank=True,
        help_text='Contact phone number'
    )
    
    address = models.TextField(
        blank=True,
        help_text='Physical address'
    )
    
    village = models.CharField(
        max_length=100,
        blank=True,
        help_text='Village or town name'
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,
        help_text='User profile photo'
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text='Whether user email has been verified'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Profile creation timestamp'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Last profile update timestamp'
    )

    def __str__(self) -> str:
        """Return human-readable string representation."""
        return f"{self.user.username} ({self.get_role_display()})"

    class Meta:
        """Model metadata configuration."""
        ordering = ['-created_at']
        verbose_name_plural = 'User Profiles'
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['-created_at']),
        ]
