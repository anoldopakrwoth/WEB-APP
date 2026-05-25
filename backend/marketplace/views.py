from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProduceListing

# home/Marketplace Feed: view all active agricultural listings
def market_feed(request):
    listings = ProduceListing.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'marketplace/feed.html', {'listings': listings})

# detailed view: see specific details and origin/target
def listing_detail(request, pk):
    listing = get_object_or_404(ProduceListing, pk=pk)
    return render(request, 'marketplace/detail.html', {'listing': listing})

# create listing: let farmers add produce
@login_required(login_url='login')
def create_listing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        village_origin = request.POST.get('village_origin')
        target_town = request.POST.get('target_town')
        image = request.FILES.get('image', None)

        # Validate inputs
        if not all([title, description, price, quantity, village_origin, target_town]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('create_listing')

        try:
            # save to database with current user as seller
            listing = ProduceListing.objects.create(
                seller=request.user,
                title=title,
                description=description,
                price=price,
                quantity=quantity,
                village_origin=village_origin,
                target_town=target_town,
            )
            if image:
                listing.image = image
                listing.save()

            messages.success(request, 'Listing created successfully!')
            return redirect('market_feed')
        except Exception as e:
            messages.error(request, f'Error creating listing: {str(e)}')
            return redirect('create_listing')

    return render(request, 'marketplace/create_listing.html')