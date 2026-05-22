# marketplace/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_feed, name='market_feed'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listing/new/', views.create_listing, name='create_listing'),
]