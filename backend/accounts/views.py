from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile


def signup(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('market_feed')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        role = request.POST.get('role', 'buyer')
        village = request.POST.get('village', '')
        phone = request.POST.get('phone', '')

        # Validation
        if not username or not email or not password:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('signup')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('signup')

        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=request.POST.get('first_name', ''),
                last_name=request.POST.get('last_name', '')
            )

            # Create user profile
            UserProfile.objects.create(
                user=user,
                role=role,
                village=village,
                phone=phone,
                is_verified=False
            )

            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return redirect('signup')

    context = {
        'roles': UserProfile.USER_ROLE_CHOICES
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('market_feed')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to dashboard if admin, else to marketplace
            if user.username == 'admin':
                return redirect('dashboard_home')
            return redirect('market_feed')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    """User profile view"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Update profile
        profile.phone = request.POST.get('phone', profile.phone)
        profile.village = request.POST.get('village', profile.village)
        profile.address = request.POST.get('address', profile.address)
        
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()

        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)
