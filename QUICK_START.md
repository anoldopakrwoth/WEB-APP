# 🚀 Quick Start Guide

## Your Agricultural Marketplace is Ready!

### ✅ Current Status
- ✅ All files organized into backend/frontend folders
- ✅ Database fully migrated and initialized  
- ✅ Admin user created (admin / admin)
- ✅ Server running at http://localhost:8000/
- ✅ All 13 templates loaded and working

---

## Start Using the System

### 1. **Access the Web App**
Open your browser and go to:
```
http://localhost:8000/
```

### 2. **Login as Admin**
- **URL**: http://localhost:8000/accounts/login/
- **Username**: `admin`
- **Password**: `admin`

### 3. **Access Admin Dashboard**
After login, visit:
```
http://localhost:8000/dashboard/
```

---

## What You Can Do

### 👤 User Management
- Create new user accounts
- Register as Farmer, Buyer, or Admin
- View all users in dashboard
- Edit user profiles
- Upload profile pictures

### 🛒 Marketplace
- **Browse**: Visit http://localhost:8000/marketplace/
- **Create Listing**: Click "Create Listing"
- **Add Details**: Product name, description, price, image
- **View Details**: Click on any product to see full details
- **Search/Filter**: Coming in future updates

### 📊 Admin Dashboard
Features available:
- **Dashboard Home**: System overview and statistics
- **User Management**: View, monitor, and manage users
- **Listing Management**: View and manage all product listings
- **System Logs**: Track all system activities
- **Analytics**: View metrics and statistics
- **Notifications**: Manage system notifications

---

## User Roles

| Role | Access |
|------|--------|
| **Admin** | Full system access, dashboard, user management, logs |
| **Farmer** | Create/manage listings, profile, marketplace |
| **Buyer** | Browse listings, profile, search |

---

## File Locations

| What | Where |
|------|-------|
| Django Code | `backend/` |
| Templates | `frontend/templates/` |
| Static Files | `frontend/static/` |
| Database | `backend/db.sqlite3` |
| User Uploads | `frontend/media/listings/` |
| Configuration | `backend/Agricultural/settings.py` |

---

## Running Commands

### Start/Stop Server
```bash
# Navigate to backend
cd backend

# Start server
python manage.py runserver 0.0.0.0:8000

# Stop: Press Ctrl+C
```

### Database Commands
```bash
cd backend

# Apply migrations
python manage.py migrate

# Create new migrations
python manage.py makemigrations

# Django shell
python manage.py shell
```

### Create New User
```bash
cd backend
python manage.py createsuperuser
```

---

## Key Pages & URLs

| Page | URL |
|------|-----|
| Home | `/` |
| Sign Up | `/accounts/signup/` |
| Login | `/accounts/login/` |
| Profile | `/accounts/profile/` |
| Marketplace | `/marketplace/` |
| Listing Details | `/marketplace/<id>/` |
| Create Listing | `/marketplace/create/` |
| Dashboard Home | `/dashboard/` |
| User Management | `/dashboard/users/` |
| Listing Management | `/dashboard/listings/` |
| System Logs | `/dashboard/logs/` |
| Analytics | `/dashboard/analytics/` |
| Notifications | `/dashboard/notifications/` |

---

## Features Overview

### ✨ Security
- CSRF protection on all forms
- Password hashing (PBKDF2)
- Session-based authentication
- SQL injection prevention (Django ORM)
- Role-based access control

### 📱 User Interface
- Bootstrap 5.3 responsive design
- Mobile-friendly templates
- Image uploads for products and profiles
- Clean, modern UI

### 💾 Database
- SQLite for development
- 10+ tables for full functionality
- Proper relationships and constraints
- Automatic timestamps on records

### 🔧 Admin Features
- System monitoring
- User activity tracking
- Performance metrics
- Notification system
- Audit logs

---

## Test Accounts

| Username | Password | Role | Purpose |
|----------|----------|------|---------|
| admin | admin | Admin | Full system access, testing dashboard |

---

## Need Help?

### Documentation Files
- **STRUCTURE.md** - Complete project structure documentation
- **ORGANIZATION_COMPLETE.md** - Reorganization summary
- **API_DOCUMENTATION.md** - API endpoints reference
- **FEATURES.md** - Detailed feature list
- **DEPLOYMENT.md** - How to deploy to production

### Common Tasks

**Create a listing:**
1. Login at `/accounts/login/`
2. Go to `/marketplace/create/`
3. Fill in product details
4. Upload product image
5. Click "Create"

**Manage users:**
1. Login as admin
2. Visit `/dashboard/users/`
3. View all users with statistics
4. Search and filter users

**View system logs:**
1. Login as admin
2. Visit `/dashboard/logs/`
3. See all system activities
4. Filter by type or date

---

## Next Steps

1. ✅ Explore the dashboard at `/dashboard/`
2. ✅ Create some test product listings
3. ✅ Test with different user roles
4. ✅ Check admin features
5. ✅ Review documentation for deployment info

---

## Troubleshooting

**Server won't start?**
```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```

**Database error?**
```bash
cd backend
python manage.py migrate
```

**Templates not found?**
- Check `frontend/templates/` exists
- Verify settings.py TEMPLATES DIRS points to correct path

**Static files missing?**
```bash
cd backend
python manage.py collectstatic
```

---

## Support

For detailed information, see the documentation files in the `docs/` folder.

---

**🎉 Your Agricultural Marketplace System is Ready to Use!**

Start by visiting: **http://localhost:8000/**
