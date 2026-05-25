# Project Structure

## Agricultural Marketplace System

This project follows a clear backend/frontend separation for better maintainability and scalability.

```
WEB APP/
├── backend/                          # Django backend application
│   ├── manage.py                     # Django management script
│   ├── db.sqlite3                    # SQLite database
│   ├── requirements.txt              # Python dependencies
│   ├── setup.py                      # Initialize admin user
│   ├── Agricultural/                 # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py              # Main configuration
│   │   ├── urls.py                  # URL routing
│   │   ├── asgi.py                  # ASGI config
│   │   └── wsgi.py                  # WSGI config
│   ├── accounts/                     # Authentication app
│   │   ├── models.py                # UserProfile model
│   │   ├── views.py                 # Auth views (signup, login, profile)
│   │   ├── forms.py                 # Auth forms
│   │   ├── signals.py               # Auto-create UserProfile
│   │   ├── urls.py                  # Auth routes
│   │   ├── admin.py                 # Admin registration
│   │   ├── apps.py
│   │   └── migrations/              # Database migrations
│   ├── marketplace/                  # Product listing app
│   │   ├── models.py                # ProduceListing model
│   │   ├── views.py                 # Feed, detail, create views
│   │   ├── forms.py                 # Listing form
│   │   ├── urls.py                  # Marketplace routes
│   │   ├── admin.py                 # Admin interface
│   │   ├── apps.py
│   │   └── migrations/              # Database migrations
│   ├── dashboard/                    # Admin dashboard app
│   │   ├── models.py                # SystemLog, SystemMetrics, Notification
│   │   ├── views.py                 # Dashboard views (6 main views)
│   │   ├── urls.py                  # Dashboard routes
│   │   ├── admin.py                 # Admin interface
│   │   ├── apps.py
│   │   └── migrations/              # Database migrations
│   └── manage.py
│
├── frontend/                         # Frontend assets and templates
│   ├── templates/                    # HTML templates
│   │   ├── base.html                # Master template (Bootstrap 5)
│   │   ├── accounts/                # Auth templates
│   │   │   ├── signup.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   │   │   └── password_reset.html
│   │   ├── marketplace/              # Marketplace templates
│   │   │   ├── feed.html            # List all listings
│   │   │   ├── detail.html          # Single listing detail
│   │   │   └── create_listing.html  # Create new listing
│   │   └── dashboard/               # Admin dashboard templates
│   │       ├── dashboard_home.html  # Dashboard overview
│   │       ├── users.html           # User management
│   │       ├── listings.html        # Listing management
│   │       ├── logs.html            # System logs view
│   │       ├── analytics.html       # Analytics & metrics
│   │       └── notifications.html   # Notifications
│   ├── static/                       # Static files (CSS, JS, images)
│   │   ├── css/                     # Custom stylesheets
│   │   ├── js/                      # JavaScript files
│   │   └── images/                  # Image assets
│   └── media/                        # User-uploaded media
│       └── listings/                # Product listing images
│
├── docs/                             # Documentation
│   ├── GITHUB_PUSH_GUIDE.md
│   ├── README.md
│   ├── API_DOCUMENTATION.md
│   ├── FEATURES.md
│   └── DEPLOYMENT.md
│
├── .git/                             # Git repository
├── .gitignore
├── .venv/                            # Python virtual environment
└── STRUCTURE.md                      # This file


```

## Technology Stack

- **Backend**: Django 6.0.5 (Python)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, JavaScript
- **Server**: Django development/production server
- **Authentication**: Django built-in auth with PBKDF2 hashing

## Key Features

### 1. **Authentication System** (accounts/)
- User registration with role selection (Farmer/Buyer/Admin)
- Login with session management
- User profile with image upload
- Password reset capability
- CSRF protection

### 2. **Marketplace** (marketplace/)
- Create product listings with images
- Browse all listings (feed)
- View listing details
- Filter/search capabilities
- Image upload for products

### 3. **Admin Dashboard** (dashboard/)
- System overview with statistics
- User management and monitoring
- Listing management
- System log viewing
- Analytics and metrics
- Notification system

### 4. **Database Models**
- **User**: Django built-in auth user
- **UserProfile**: Extended user info (role, phone, address, profile picture)
- **ProduceListing**: Agricultural products
- **SystemLog**: Activity tracking
- **SystemMetrics**: System statistics
- **Notification**: User notifications

## Running the Application

### Development Server

```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```

Visit: http://localhost:8000

### Admin Credentials
- **Username**: admin
- **Password**: admin

### Creating Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

## API Routes

### Authentication
- `GET /accounts/signup/` - Sign up page
- `POST /accounts/signup/` - Submit signup form
- `GET /accounts/login/` - Login page
- `POST /accounts/login/` - Submit login
- `GET /accounts/logout/` - Logout
- `GET /accounts/profile/` - User profile

### Marketplace
- `GET /marketplace/` - View all listings (feed)
- `GET /marketplace/<id>/` - View listing detail
- `GET /marketplace/create/` - Create listing page
- `POST /marketplace/create/` - Submit new listing

### Admin Dashboard
- `GET /dashboard/` - Dashboard home
- `GET /dashboard/users/` - User management
- `GET /dashboard/listings/` - Listing management
- `GET /dashboard/logs/` - System logs
- `GET /dashboard/analytics/` - Analytics
- `GET /dashboard/notifications/` - Notifications

## File Organization Best Practices

### Backend (server-side logic)
- Django apps with models, views, forms, URLs
- Database migrations
- Authentication logic
- Business logic

### Frontend (client-side assets)
- HTML templates (centralized in templates/)
- Static CSS/JS (in static/)
- Media uploads (in media/)
- Bootstrap components

## Security Features

✅ CSRF Protection
✅ Password Hashing (PBKDF2)
✅ SQL Injection Prevention (ORM)
✅ Session Management
✅ Admin authentication required for dashboard
✅ User role-based access control

## Future Enhancements

- [ ] API endpoints (REST API)
- [ ] Email notifications
- [ ] Advanced search and filters
- [ ] Payment integration
- [ ] Chat/messaging system
- [ ] Review and ratings system
- [ ] Mobile app support
- [ ] Caching layer (Redis)
