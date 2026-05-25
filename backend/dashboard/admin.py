from django.contrib import admin
from .models import SystemLog, SystemMetrics, Notification


@admin.register(SystemLog)
class SystemLogAdmin(admin.ModelAdmin):
    list_display = ('log_type', 'user', 'timestamp', 'message')
    list_filter = ('log_type', 'timestamp')
    search_fields = ('message', 'user__username')
    readonly_fields = ('timestamp', 'message')


@admin.register(SystemMetrics)
class SystemMetricsAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'total_users', 'total_listings', 'active_users')
    list_filter = ('timestamp',)
    readonly_fields = ('timestamp',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'user', 'is_read', 'created_at')
    list_filter = ('priority', 'is_read', 'created_at')
    search_fields = ('title', 'message')
