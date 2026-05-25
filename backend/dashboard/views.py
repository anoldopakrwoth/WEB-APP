from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from marketplace.models import ProduceListing
from accounts.models import UserProfile
from .models import SystemLog, SystemMetrics, Notification


def is_admin(user):
    """Check if user is admin"""
    return user.username == 'admin' and user.is_staff


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='market_feed')
def dashboard_home(request):
    """Admin dashboard home page"""
    
    # Calculate metrics
    total_users = User.objects.count()
    total_listings = ProduceListing.objects.count()
    active_listings = ProduceListing.objects.filter(is_available=True).count()
    total_farmers = UserProfile.objects.filter(role='farmer').count()
    total_buyers = UserProfile.objects.filter(role='buyer').count()
    
    # Get last 30 days data
    thirty_days_ago = timezone.now() - timedelta(days=30)
    new_users_30d = User.objects.filter(date_joined__gte=thirty_days_ago).count()
    new_listings_30d = ProduceListing.objects.filter(created_at__gte=thirty_days_ago).count()
    
    # Get recent logs
    recent_logs = SystemLog.objects.all()[:10]
    
    # Get system metrics
    try:
        latest_metrics = SystemMetrics.objects.latest('timestamp')
    except SystemMetrics.DoesNotExist:
        latest_metrics = None

    # Get unread notifications
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False).count()

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
        'unread_notifications': unread_notifications,
    }
    
    return render(request, 'dashboard/home.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='market_feed')
def user_management(request):
    """Manage all users"""
    users = User.objects.all().prefetch_related('profile')
    
    # Filter by role if requested
    role_filter = request.GET.get('role')
    if role_filter:
        users = users.filter(profile__role=role_filter)
    
    # Search functionality
    search_query = request.GET.get('q')
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
@user_passes_test(is_admin, login_url='market_feed')
def listing_management(request):
    """Manage all listings"""
    listings = ProduceListing.objects.all().select_related('seller')
    
    # Filter by availability
    status_filter = request.GET.get('status')
    if status_filter == 'active':
        listings = listings.filter(is_available=True)
    elif status_filter == 'inactive':
        listings = listings.filter(is_available=False)
    
    # Search functionality
    search_query = request.GET.get('q')
    if search_query:
        listings = listings.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(village_origin__icontains=search_query)
        )

    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    listings = listings.order_by(sort_by)

    context = {
        'listings': listings,
        'status_filter': status_filter,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    
    return render(request, 'dashboard/listing_management.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='market_feed')
def system_logs(request):
    """View system logs"""
    logs = SystemLog.objects.all()
    
    # Filter by log type
    log_type_filter = request.GET.get('type')
    if log_type_filter:
        logs = logs.filter(log_type=log_type_filter)
    
    # Search functionality
    search_query = request.GET.get('q')
    if search_query:
        logs = logs.filter(
            Q(message__icontains=search_query) |
            Q(user__username__icontains=search_query)
        )
    
    # Date filter
    date_filter = request.GET.get('date')
    if date_filter == '24h':
        logs = logs.filter(timestamp__gte=timezone.now() - timedelta(hours=24))
    elif date_filter == '7d':
        logs = logs.filter(timestamp__gte=timezone.now() - timedelta(days=7))
    elif date_filter == '30d':
        logs = logs.filter(timestamp__gte=timezone.now() - timedelta(days=30))

    context = {
        'logs': logs[:500],  # Show last 500 logs
        'log_types': SystemLog.LOG_TYPES,
        'log_type_filter': log_type_filter,
        'search_query': search_query,
        'date_filter': date_filter,
    }
    
    return render(request, 'dashboard/system_logs.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='market_feed')
def analytics(request):
    """View analytics and reports"""
    # User statistics
    total_users = User.objects.count()
    farmers = UserProfile.objects.filter(role='farmer').count()
    buyers = UserProfile.objects.filter(role='buyer').count()
    
    # Listing statistics
    total_listings = ProduceListing.objects.count()
    active_listings = ProduceListing.objects.filter(is_available=True).count()
    
    # Timeline data - last 30 days
    thirty_days_ago = timezone.now() - timedelta(days=30)
    daily_new_users = []
    daily_new_listings = []
    
    for i in range(30, 0, -1):
        date = timezone.now() - timedelta(days=i)
        next_date = date + timedelta(days=1)
        
        users_count = User.objects.filter(
            date_joined__gte=date,
            date_joined__lt=next_date
        ).count()
        
        listings_count = ProduceListing.objects.filter(
            created_at__gte=date,
            created_at__lt=next_date
        ).count()
        
        daily_new_users.append(users_count)
        daily_new_listings.append(listings_count)
    
    # Get top sellers
    top_sellers = User.objects.filter(
        listings__is_available=True
    ).annotate(
        listing_count=Count('listings')
    ).order_by('-listing_count')[:5]
    
    # Get most popular produce types
    popular_produces = ProduceListing.objects.values('title').annotate(
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
        'top_sellers': top_sellers,
        'popular_produces': popular_produces,
    }
    
    return render(request, 'dashboard/analytics.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin, login_url='market_feed')
def notifications(request):
    """View and manage notifications"""
    admin_user = request.user
    notifs = Notification.objects.filter(user=admin_user)
    
    # Mark as read if requested
    if request.method == 'POST':
        notif_id = request.POST.get('notif_id')
        action = request.POST.get('action')
        
        try:
            notif = Notification.objects.get(id=notif_id, user=admin_user)
            if action == 'read':
                notif.is_read = True
                notif.save()
            elif action == 'delete':
                notif.delete()
        except Notification.DoesNotExist:
            pass

    unread = notifs.filter(is_read=False)
    read = notifs.filter(is_read=True)

    context = {
        'unread': unread,
        'read': read,
        'total_unread': unread.count(),
    }
    
    return render(request, 'dashboard/notifications.html', context)
