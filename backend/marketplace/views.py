"""
Marketplace views for agricultural produce listings.

This module handles:
- Displaying the marketplace feed of all active listings
- Viewing detailed information about specific listings
- Creating new produce listings
"""

from decimal import Decimal, InvalidOperation
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from common import validate_image_upload
from .models import ProduceListing


def _validation_error_message(error: ValidationError) -> str:
    """Return a clean message string from a Django ValidationError."""
    return ' '.join(error.messages)


def _validate_price(price_str: str) -> Decimal:
    """
    Validate and convert price string to Decimal.
    
    Args:
        price_str: String representation of price
        
    Returns:
        Decimal: Validated price value
        
    Raises:
        ValidationError: If price is invalid
    """
    try:
        price = Decimal(price_str)
        if not price.is_finite():
            raise ValidationError('Price must be a valid number.')
        if price <= 0:
            raise ValidationError('Price must be greater than zero.')
        if price > Decimal('999999.99'):
            raise ValidationError('Price is too large.')
        if price.as_tuple().exponent < -2:
            raise ValidationError('Price can include at most 2 decimal places.')
        return price
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError('Price must be a valid number.') from e


def _validate_quantity(quantity_str: str) -> str:
    """
    Validate quantity string.
    
    Args:
        quantity_str: String representation of quantity
        
    Returns:
        str: Validated quantity string
        
    Raises:
        ValidationError: If quantity is invalid
    """
    if not quantity_str or len(quantity_str) > 50:
        raise ValidationError(
            'Quantity must be provided and less than 50 characters.'
        )
    return quantity_str.strip()


@require_http_methods(['GET'])
def market_feed(request: HttpRequest) -> HttpResponse:
    """
    Display the marketplace feed of all active agricultural listings.
    
    This view shows all currently available produce listings, ordered by
    most recent first. Farmers and buyers can browse available products.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered feed.html template with listings context
    """
    listings = ProduceListing.objects.filter(
        is_available=True
    ).order_by('-created_at').select_related('seller')
    
    context = {'listings': listings}
    return render(request, 'marketplace/feed.html', context)


@require_http_methods(['GET'])
def listing_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Display detailed information about a specific produce listing.
    
    Shows full product details including seller information, location,
    price, quantity, and availability status.
    
    Args:
        request: HttpRequest object
        pk: Primary key of the ProduceListing object
        
    Returns:
        HttpResponse: Rendered detail.html template with listing context
        
    Raises:
        Http404: If listing does not exist or is unavailable
    """
    listing = get_object_or_404(ProduceListing, pk=pk, is_available=True)
    
    context = {'listing': listing}
    return render(request, 'marketplace/detail.html', context)


@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def create_listing(request: HttpRequest) -> HttpResponse:
    """
    Create a new produce listing.
    
    GET: Display the listing creation form.
    POST: Validate input and save new listing to database.
    
    Only authenticated users (logged-in farmers) can create listings.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered create_listing.html form or redirect to feed
    """
    if request.method == 'POST':
        # Get and validate form data
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        price_str = request.POST.get('price', '').strip()
        quantity_str = request.POST.get('quantity', '').strip()
        village_origin = request.POST.get('village_origin', '').strip()
        target_town = request.POST.get('target_town', '').strip()
        image = request.FILES.get('image', None)

        # Validate all required fields
        if not all([title, description, price_str, quantity_str,
                    village_origin, target_town]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('create_listing')

        # Validate text fields length
        if len(title) > 200:
            messages.error(request, 'Title must be less than 200 characters.')
            return redirect('create_listing')
        if len(village_origin) > 100 or len(target_town) > 100:
            messages.error(
                request,
                'Village and target town must be less than 100 characters.'
            )
            return redirect('create_listing')

        try:
            price = _validate_price(price_str)
            quantity = _validate_quantity(quantity_str)
            validate_image_upload(image)

            ProduceListing.objects.create(
                seller=request.user,
                title=title,
                description=description,
                price=price,
                quantity=quantity,
                village_origin=village_origin,
                target_town=target_town,
                image=image if image else None,
            )

            messages.success(request, 'Listing created successfully!')
            return redirect('market_feed')
            
        except ValidationError as error:
            messages.error(request, _validation_error_message(error))
            return redirect('create_listing')
        except Exception:
            messages.error(
                request,
                'An error occurred while creating the listing. Please try again.'
            )
            return redirect('create_listing')

    return render(request, 'marketplace/create_listing.html')
