"""
Dashboard and monitoring models for system administration.

This module defines models for tracking system logs, metrics, and
notifications in the administrative dashboard.
"""

from django.db import models
from django.contrib.auth.models import User


class SystemLog(models.Model):
    """
    Track all system activities for monitoring and auditing.
    
    Attributes:
        timestamp (DateTime): When the event occurred
        log_type (str): Category of event (login, signup, error, etc.)
        user (ForeignKey): User associated with the event (optional)
        message (str): Description of the event
        ip_address (str): IP address of the request
        details (JSON): Additional structured data
    """

    LOG_TYPES = [
        ('user_login', 'User Login'),
        ('user_signup', 'User Signup'),
        ('listing_created', 'Listing Created'),
        ('listing_deleted', 'Listing Deleted'),
        ('listing_updated', 'Listing Updated'),
        ('error', 'Error'),
        ('other', 'Other'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    log_type = models.CharField(max_length=50, choices=LOG_TYPES)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='User associated with this log entry'
    )
    message = models.TextField(help_text='Log message')
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        help_text='IP address of the request'
    )
    details = models.JSONField(
        default=dict,
        blank=True,
        help_text='Additional structured data'
    )

    def __str__(self) -> str:
        """Return human-readable string representation."""
        return f"{self.get_log_type_display()} - {self.timestamp}"

    class Meta:
        """Model metadata configuration."""
        ordering = ['-timestamp']
        verbose_name_plural = 'System Logs'
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['log_type']),
        ]


class SystemMetrics(models.Model):
    """
    Track system metrics for dashboard monitoring.
    
    Records system-wide statistics about users, listings, and
    resource usage at specific points in time.
    
    Attributes:
        timestamp (DateTime): When metrics were recorded
        total_users (int): Total number of users
        total_listings (int): Total number of listings
        active_listings (int): Number of active listings
        total_revenue (Decimal): Total platform revenue
        cpu_usage (float): CPU usage percentage
        memory_usage (float): Memory usage percentage
        active_users (int): Users active in last 24 hours
    """

    timestamp = models.DateTimeField(auto_now_add=True)
    total_users = models.IntegerField(default=0)
    total_listings = models.IntegerField(default=0)
    active_listings = models.IntegerField(default=0)
    total_revenue = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )
    cpu_usage = models.FloatField(
        default=0,
        help_text='CPU usage percentage'
    )
    memory_usage = models.FloatField(
        default=0,
        help_text='Memory usage percentage'
    )
    active_users = models.IntegerField(
        default=0,
        help_text='Users active in last 24 hours'
    )

    def __str__(self) -> str:
        """Return human-readable string representation."""
        return f"Metrics - {self.timestamp}"

    class Meta:
        """Model metadata configuration."""
        ordering = ['-timestamp']
        verbose_name_plural = 'System Metrics'
        indexes = [
            models.Index(fields=['-timestamp']),
        ]


class Notification(models.Model):
    """
    System notifications for administrators.
    
    Attributes:
        title (str): Notification title
        message (str): Notification message
        priority (str): Urgency level (low, medium, high, critical)
        user (ForeignKey): Admin user receiving the notification
        is_read (bool): Whether notification has been read
        created_at (DateTime): When notification was created
    """

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    title = models.CharField(
        max_length=200,
        help_text='Notification title'
    )
    message = models.TextField(
        help_text='Notification message'
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text='Priority level'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        help_text='Target admin user'
    )
    is_read = models.BooleanField(
        default=False,
        help_text='Whether notification has been read'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        """Return human-readable string representation."""
        return f"{self.title} - {self.get_priority_display()}"

    class Meta:
        """Model metadata configuration."""
        ordering = ['-created_at']
        verbose_name_plural = 'Notifications'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['user', 'is_read']),
        ]
