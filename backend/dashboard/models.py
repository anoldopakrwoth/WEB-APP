from django.db import models
from django.contrib.auth.models import User


class SystemLog(models.Model):
    """Track all system activities for monitoring"""
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.log_type} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['log_type']),
        ]


class SystemMetrics(models.Model):
    """Track system metrics for dashboard monitoring"""
    timestamp = models.DateTimeField(auto_now_add=True)
    total_users = models.IntegerField(default=0)
    total_listings = models.IntegerField(default=0)
    active_listings = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cpu_usage = models.FloatField(default=0, help_text="CPU usage percentage")
    memory_usage = models.FloatField(default=0, help_text="Memory usage percentage")
    active_users = models.IntegerField(default=0, help_text="Users active in last 24 hours")

    def __str__(self):
        return f"Metrics - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'System Metrics'


class Notification(models.Model):
    """System notifications for admins"""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.priority}"

    class Meta:
        ordering = ['-created_at']
