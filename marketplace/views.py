from django.shortcuts import render, get_object_or_404, redirect
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
def create_listing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        village_origin = request.POST.get('village_origin')
        target_town = request.POST.get('target_town')
        image = request.FILES.get('image', None)
        seller_name = request.POST.get('seller_name', 'Anonymous Farmer')

        # Get or create a demo user for the seller
        from django.contrib.auth.models import User
        seller, created = User.objects.get_or_create(username=seller_name, defaults={'email': f'{seller_name}@agrilink.local'})

        # save to database
        listing = ProduceListing.objects.create(
            seller=seller,
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
        return redirect('market_feed')
    return render(request, 'marketplace/create_listing.html')