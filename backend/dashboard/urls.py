# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('users/', views.user_management, name='user_management'),
    path('listings/', views.listing_management, name='listing_management'),
    path('logs/', views.system_logs, name='system_logs'),
    path('analytics/', views.analytics, name='analytics'),
    path('notifications/', views.notifications, name='notifications'),
]
