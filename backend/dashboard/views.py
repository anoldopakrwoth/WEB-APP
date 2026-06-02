"""
Admin dashboard views for system administration.

This module provides comprehensive administrative dashboards for
managing users, listings, system logs, analytics, and notifications.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from datetime import timedelta
from common import is_admin_user
from marketplace.models import ProduceListing
from accounts.models import UserProfile
from .models import SystemLog, SystemMetrics, Notification


LISTING_SORT_OPTIONS = {
    '-created_at': '-created_at',
    'created_at': 'created_at',
    'title': 'title',
    '-price': '-price',
    'price': 'price',
}


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
def dashboard_home(request: HttpRequest) -> HttpResponse:
    """
    Admin dashboard home page.
    
    Displays key metrics and recent activity for system administrators.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/home.html template
    """
    # Calculate metrics
    total_users = User.objects.count()
    total_listings = ProduceListing.objects.count()
    active_listings = ProduceListing.objects.filter(is_available=True).count()
    total_farmers = UserProfile.objects.filter(role='farmer').count()
    total_buyers = UserProfile.objects.filter(role='buyer').count()
    
    # Get last 30 days data
    thirty_days_ago = timezone.now() - timedelta(days=30)
    new_users_30d = User.objects.filter(date_joined__gte=thirty_days_ago).count()
    new_listings_30d = ProduceListing.objects.filter(
        created_at__gte=thirty_days_ago
    ).count()
    
    # Get recent logs
    recent_logs = SystemLog.objects.all()[:10]
    
    # Get system metrics
    try:
        latest_metrics = SystemMetrics.objects.latest('timestamp')
    except SystemMetrics.DoesNotExist:
        latest_metrics = None

    # Get unread notifications count
    unread_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    context = {
        'total_users': total_users,
        'total_listings': total_listings,
        'active_listings': active_listings,
        'total_farmers': total_farmers,
        'total_buyers': total_buyers,
        'new_users_30d': new_users_30d,
        'new_listings_30d': new_listings_30d,
        'recent_logs': recent_logs,
        'latest_metrics': latest_metrics,
        'unread_notifications': unread_count,
    }
    
    return render(request, 'dashboard/home.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
def user_management(request: HttpRequest) -> HttpResponse:
    """
    Manage all platform users.
    
    Displays list of all users with filtering and search capabilities.
    Admins can view user information and roles.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/user_management.html template
    """
    users = User.objects.all().select_related('profile')
    
    # Filter by role if requested
    role_filter = request.GET.get('role')
    if role_filter:
        users = users.filter(profile__role=role_filter)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )

    context = {
        'users': users,
        'roles': UserProfile.USER_ROLE_CHOICES,
        'current_role': role_filter,
        'search_query': search_query,
    }
    
    return render(request, 'dashboard/user_management.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
def listing_management(request: HttpRequest) -> HttpResponse:
    """
    Manage all produce listings on the platform.
    
    Displays list of all listings with filtering and search capabilities.
    Admins can view and manage listing availability.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/listing_management.html template
    """
    listings = ProduceListing.objects.all().select_related('seller')
    
    # Filter by availability
    status_filter = request.GET.get('status')
    if status_filter == 'active':
        listings = listings.filter(is_available=True)
    elif status_filter == 'inactive':
        listings = listings.filter(is_available=False)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(village_origin__icontains=search_query)
        )

    # Sorting
    requested_sort = request.GET.get('sort', '-created_at')
    sort_by = LISTING_SORT_OPTIONS.get(requested_sort, '-created_at')
    listings = listings.order_by(sort_by)

    context = {
        'listings': listings,
        'status_filter': status_filter,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    
    return render(request, 'dashboard/listing_management.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
def system_logs(request: HttpRequest) -> HttpResponse:
    """
    View system activity logs.
    
    Displays system logs for auditing and monitoring with filtering
    by log type, search query, and date range.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/system_logs.html template
    """
    logs = SystemLog.objects.all()
    
    # Filter by log type
    log_type_filter = request.GET.get('type', '')
    if log_type_filter:
        logs = logs.filter(log_type=log_type_filter)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        logs = logs.filter(
            Q(message__icontains=search_query) |
            Q(user__username__icontains=search_query)
        )
    
    # Date filter
    date_filter = request.GET.get('date', '')
    if date_filter == '24h':
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(hours=24)
        )
    elif date_filter == '7d':
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(days=7)
        )
    elif date_filter == '30d':
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(days=30)
        )

    context = {
        'logs': logs[:500],  # Show last 500 logs
        'log_types': SystemLog.LOG_TYPES,
        'log_type_filter': log_type_filter,
        'search_query': search_query,
        'date_filter': date_filter,
    }
    
    return render(request, 'dashboard/system_logs.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
def analytics(request: HttpRequest) -> HttpResponse:
    """
    View analytics and reports.
    
    Displays comprehensive analytics including user statistics, listing
    statistics, timeline data, top sellers, and popular produce types.
    
    Uses database aggregation to avoid N+1 query problems.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/analytics.html template
    """
    # User statistics
    total_users = User.objects.count()
    farmers = UserProfile.objects.filter(role='farmer').count()
    buyers = UserProfile.objects.filter(role='buyer').count()
    
    # Listing statistics
    total_listings = ProduceListing.objects.count()
    active_listings = ProduceListing.objects.filter(is_available=True).count()
    
    # OPTIMIZED: Use aggregation instead of loop (fixes N+1 problem)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    users_30d = {
        item['date_joined__date']: item['count']
        for item in User.objects.filter(
            date_joined__gte=thirty_days_ago
        ).values('date_joined__date').annotate(count=Count('id'))
    }

    listings_30d = {
        item['created_at__date']: item['count']
        for item in ProduceListing.objects.filter(
            created_at__gte=thirty_days_ago
        ).values('created_at__date').annotate(count=Count('id'))
    }

    daily_new_users = []
    daily_new_listings = []

    for i in range(30):
        current_date = (timezone.now() - timedelta(days=29 - i)).date()
        daily_new_users.append(users_30d.get(current_date, 0))
        daily_new_listings.append(listings_30d.get(current_date, 0))

    total_new_users_30d = sum(daily_new_users)
    total_new_listings_30d = sum(daily_new_listings)

    top_sellers = User.objects.filter(
        listings__is_available=True,
        listings__created_at__gte=thirty_days_ago,
    ).annotate(
        listing_count=Count('listings', distinct=True)
    ).order_by('-listing_count')[:5]

    popular_produces = ProduceListing.objects.filter(
        created_at__gte=thirty_days_ago
    ).values('title').annotate(
        count=Count('id')
    ).order_by('-count')[:5]

    context = {
        'total_users': total_users,
        'farmers': farmers,
        'buyers': buyers,
        'total_listings': total_listings,
        'active_listings': active_listings,
        'daily_new_users': daily_new_users,
        'daily_new_listings': daily_new_listings,
        'total_new_users_30d': total_new_users_30d,
        'total_new_listings_30d': total_new_listings_30d,
        'top_sellers': top_sellers,
        'popular_produces': popular_produces,
    }

    return render(request, 'dashboard/analytics.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin_user, login_url='market_feed')
@require_http_methods(['GET', 'POST'])
def notifications(request: HttpRequest) -> HttpResponse:
    """
    View and manage administrator notifications.
    
    GET: Display all notifications (read and unread)
    POST: Mark notification as read or delete
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered dashboard/notifications.html template
    """
    admin_user = request.user

    if request.method == 'POST':
        notif_id = request.POST.get('notif_id')
        action = request.POST.get('action')

        if notif_id and action in {'read', 'delete'}:
            try:
                notif = Notification.objects.get(id=notif_id, user=admin_user)
                if action == 'read':
                    notif.is_read = True
                    notif.save(update_fields=['is_read'])
                else:
                    notif.delete()
            except (Notification.DoesNotExist, ValueError):
                pass
        return redirect('notifications')

    notifs = Notification.objects.filter(user=admin_user)
    unread = notifs.filter(is_read=False)
    read = notifs.filter(is_read=True)

    context = {
        'unread': unread,
        'read': read,
        'total_unread': unread.count(),
    }

    return render(request, 'dashboard/notifications.html', context)
