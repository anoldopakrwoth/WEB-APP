"""
User authentication and profile management views.

This module handles user authentication (signup, login, logout) and
profile management for farmers and buyers on the platform.
"""

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import validate_email
from django.db import transaction
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from common import is_admin_user, validate_image_upload
from .models import UserProfile


username_validator = UnicodeUsernameValidator()


def _validation_error_message(error: ValidationError) -> str:
    """Return a clean message string from a Django ValidationError."""
    return ' '.join(error.messages)


def _safe_next_url(request: HttpRequest) -> str | None:
    """
    Extract and validate the 'next' redirect URL from request.
    
    Prevents open redirect vulnerabilities by validating that the URL
    belongs to the current host and uses secure protocols.
    
    Args:
        request: HttpRequest object
        
    Returns:
        str or None: Safe redirect URL or None if invalid
    """
    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url
    return None


def _validate_username(username: str) -> str:
    """
    Validate username format and availability.
    
    Args:
        username: Username to validate
        
    Returns:
        str: Validated username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username or len(username) < 3:
        raise ValidationError(
            'Username must be at least 3 characters long.'
        )
    if len(username) > 150:
        raise ValidationError(
            'Username must be less than 150 characters.'
        )
    username_validator(username)
    if User.objects.filter(username__iexact=username).exists():
        raise ValidationError('Username already exists.')
    
    return username


def _validate_email_address(email: str) -> str:
    """
    Validate email format and availability.
    
    Args:
        email: Email address to validate
        
    Returns:
        str: Validated email
        
    Raises:
        ValidationError: If email is invalid
    """
    if not email:
        raise ValidationError('Please enter a valid email address.')

    validate_email(email)

    if User.objects.filter(email__iexact=email).exists():
        raise ValidationError('Email already registered.')
    
    return email.lower()


def _validate_password(password: str, password_confirm: str) -> str:
    """
    Validate password strength and confirmation.
    
    Args:
        password: Password to validate
        password_confirm: Password confirmation
        
    Returns:
        str: Validated password
        
    Raises:
        ValidationError: If password is invalid
    """
    if password != password_confirm:
        raise ValidationError('Passwords do not match.')
    
    validate_password(password)
    
    return password


@require_http_methods(['GET', 'POST'])
def signup(request: HttpRequest) -> HttpResponse:
    """
    User registration/signup view.
    
    GET: Display signup form
    POST: Validate form data and create new user account with profile
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered signup.html or redirect to login
    """
    if request.user.is_authenticated:
        if is_admin_user(request.user):
            return redirect('dashboard_home')
        return redirect('market_feed')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')
        role = request.POST.get('role', 'buyer')
        village = request.POST.get('village', '').strip()
        phone = request.POST.get('phone', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()

        try:
            # Validate all input fields
            username = _validate_username(username)
            email = _validate_email_address(email)
            password = _validate_password(password, password_confirm)
            
            # Validate role
            if role not in {'farmer', 'buyer'}:
                role = 'buyer'

            with transaction.atomic():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                profile, _ = UserProfile.objects.get_or_create(user=user)
                profile.role = role
                profile.village = village
                profile.phone = phone
                profile.is_verified = False
                profile.save()

            messages.success(
                request,
                'Account created successfully! Please log in.'
            )
            return redirect('login')

        except ValidationError as error:
            messages.error(request, _validation_error_message(error))
            return redirect('signup')
        except Exception:
            messages.error(
                request,
                'An error occurred during registration. Please try again.'
            )
            return redirect('signup')

    context = {
        'roles': UserProfile.USER_ROLE_CHOICES
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login_view(request: HttpRequest) -> HttpResponse:
    """
    User login view.
    
    GET: Display login form
    POST: Authenticate user and create session
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered login.html or redirect to appropriate page
    """
    if request.user.is_authenticated:
        next_url = _safe_next_url(request)
        if next_url:
            return redirect(next_url)
        if is_admin_user(request.user):
            return redirect('dashboard_home')
        return redirect('market_feed')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip().lower()
        password = request.POST.get('password', '').lower()

        if not username or not password:
            messages.error(request, 'Please enter username and password.')
            return redirect('login')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = _safe_next_url(request)
            if next_url:
                return redirect(next_url)
            # Redirect based on user role
            if is_admin_user(user):
                return redirect('dashboard_home')
            return redirect('market_feed')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


@require_http_methods(['POST'])
def logout_view(request: HttpRequest) -> HttpResponse:
    """
    User logout view.
    
    Clears user session and redirects to login page.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Redirect to login page
    """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def profile(request: HttpRequest) -> HttpResponse:
    """
    User profile management view.
    
    GET: Display user profile with current information
    POST: Update user profile information
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered profile.html or redirect to profile
    """
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Update profile fields
        phone = request.POST.get('phone', '').strip()
        village = request.POST.get('village', '').strip()
        address = request.POST.get('address', '').strip()

        # Validate profile text fields before saving.
        if phone and len(phone) > 15:
            messages.error(request, 'Phone number must be less than 15 characters.')
            return redirect('profile')
        if village and len(village) > 100:
            messages.error(request, 'Village/Town must be less than 100 characters.')
            return redirect('profile')

        profile.phone = phone
        profile.village = village
        profile.address = address
        
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            try:
                validate_image_upload(profile_picture)
            except ValidationError as error:
                messages.error(request, _validation_error_message(error))
                return redirect('profile')
            profile.profile_picture = profile_picture

        profile.save()

        # Update user information
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()

        request.user.first_name = first_name
        request.user.last_name = last_name
        if email:
            # Validate email if changed
            if email != request.user.email:
                try:
                    validate_email(email)
                except ValidationError as error:
                    messages.error(request, _validation_error_message(error))
                    return redirect('profile')
                if User.objects.filter(email__iexact=email).exclude(
                    pk=request.user.pk
                ).exists():
                    messages.error(request, 'Email already in use.')
                    return redirect('profile')
            request.user.email = email.lower()

        request.user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile.html', context)
