#!/usr/bin/env python
"""
Initial setup script for AgriLink system.
Run this after migrations to set up the admin user and initial data.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agricultural.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile

def create_admin_user():
    """Create admin user with credentials: admin/admin"""
    if User.objects.filter(username='admin').exists():
        print("✓ Admin user already exists")
        return
    
    try:
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@agrilink.local',
            password='admin',
            first_name='Admin',
            last_name='User'
        )
        
        # Create user profile for admin
        UserProfile.objects.create(
            user=admin_user,
            role='admin',
            village='System',
            is_verified=True
        )
        
        print("✓ Admin user created successfully")
        print("  Username: admin")
        print("  Password: admin")
        return admin_user
    except Exception as e:
        print(f"✗ Error creating admin user: {str(e)}")
        return None

def create_sample_users():
    """Create sample farmer and buyer users"""
    users_created = []
    
    # Create sample farmer
    if not User.objects.filter(username='farmer1').exists():
        try:
            farmer = User.objects.create_user(
                username='farmer1',
                email='farmer1@agrilink.local',
                password='password123',
                first_name='John',
                last_name='Farmer'
            )
            UserProfile.objects.create(
                user=farmer,
                role='farmer',
                village='Mukono',
                phone='+256701234567',
                is_verified=True
            )
            users_created.append(('farmer1', 'farmer'))
            print("✓ Sample farmer user created: farmer1 / password123")
        except Exception as e:
            print(f"✗ Error creating farmer user: {str(e)}")
    
    # Create sample buyer
    if not User.objects.filter(username='buyer1').exists():
        try:
            buyer = User.objects.create_user(
                username='buyer1',
                email='buyer1@agrilink.local',
                password='password123',
                first_name='Jane',
                last_name='Buyer'
            )
            UserProfile.objects.create(
                user=buyer,
                role='buyer',
                village='Kampala',
                phone='+256702345678',
                is_verified=True
            )
            users_created.append(('buyer1', 'buyer'))
            print("✓ Sample buyer user created: buyer1 / password123")
        except Exception as e:
            print(f"✗ Error creating buyer user: {str(e)}")
    
    return users_created

def main():
    print("\n" + "="*50)
    print("AgriLink System Initialization")
    print("="*50 + "\n")
    
    # Create admin user
    print("Setting up admin user...")
    create_admin_user()
    
    # Create sample users
    print("\nCreating sample users...")
    create_sample_users()
    
    print("\n" + "="*50)
    print("Initialization Complete!")
    print("="*50)
    print("\n✓ Database setup completed successfully")
    print("✓ Admin user ready: admin / admin")
    print("✓ Sample users ready for testing")
    print("\nYou can now:")
    print("  1. Run: python manage.py runserver")
    print("  2. Visit: http://127.0.0.1:8000")
    print("  3. Login with admin/admin to access the dashboard")
    print("\n")

if __name__ == '__main__':
    main()
