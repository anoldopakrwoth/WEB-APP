# ⚡ QUICK REFERENCE CARD

## 🚀 START THE APPLICATION

```bash
cd backend
python manage.py runserver 0.0.0.0:8000
```

**Access**: http://localhost:8000/

---

## 👤 DEFAULT ADMIN ACCOUNT

**Username**: `admin`  
**Password**: `admin`

---

## 📍 KEY URLS

| Purpose | URL |
|---------|-----|
| Home/Marketplace | http://localhost:8000/ |
| Admin Dashboard | http://localhost:8000/dashboard/ |
| Sign Up | http://localhost:8000/accounts/signup/ |
| Login | http://localhost:8000/accounts/login/ |
| Profile | http://localhost:8000/accounts/profile/ |
| Post Product | http://localhost:8000/marketplace/listing/new/ |

---

## 🎯 NAVIGATION FEATURES

### **In Navbar (Top of every page)**

**For Everyone**:
- 🌾 Logo (click → Home)
- 🏠 Marketplace

**For Unauthenticated Users**:
- 🔐 Login
- 👥 Sign Up

**For Logged-in Users**:
- 📝 Post Harvest (Post new products)
- 👤 User Menu (Profile, Logout)

**For Admin Only**:
- 📊 Dashboard

---

## 🔄 USER FLOWS

### **New User**
```
1. Click "Sign Up"
2. Fill in registration
3. Create account
4. Login with credentials
5. See marketplace
```

### **Create Product (Farmer)**
```
1. Login as farmer
2. Click "Post Harvest"
3. Fill product details
4. Upload image
5. Publish → Listed on marketplace
```

### **Admin Dashboard**
```
1. Login as admin
2. Click "Dashboard" in navbar
3. View:
   - System overview
   - User management
   - Product management
   - System logs
   - Analytics
   - Notifications
```

---

## 📱 RESPONSIVE DESIGN

✅ Works on:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 767px)

**Navbar collapses on mobile** - Click hamburger menu ☰

---

## 🔐 SECURITY

- ✅ Password hashing
- ✅ CSRF protection
- ✅ Session-based auth
- ✅ Admin-only dashboard
- ✅ SQL injection prevention

---

## 📊 DATABASE

**Location**: `backend/db.sqlite3`

**Tables** (10+):
- Users & Profiles
- Products/Listings
- System Logs
- Metrics & Notifications
- Admin data

**Status**: ✅ Ready to use

---

## 📁 PROJECT STRUCTURE

```
WEB APP/
├── backend/
│   ├── Agricultural/     (Django settings)
│   ├── marketplace/      (Products)
│   ├── accounts/        (Auth)
│   ├── dashboard/       (Admin)
│   └── db.sqlite3
│
└── frontend/
    ├── templates/       (HTML pages)
    ├── static/         (CSS, JS)
    └── media/          (Uploads)
```

---

## 🛠️ COMMON COMMANDS

```bash
# Start server
python manage.py runserver 0.0.0.0:8000

# Create new admin
python manage.py createsuperuser

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Django shell
python manage.py shell

# Clear database (WARNING!)
python manage.py flush
```

---

## 🎨 COLOR SCHEME

- **Primary**: Green (#2ecc71)
- **Secondary**: Dark Green (#27ae60)
- **Text**: Dark (#333)
- **Background**: White (#FFF)

---

## 📝 FEATURES

✅ View Products  
✅ Create Account  
✅ Login/Logout  
✅ Post Products (Farmers)  
✅ Edit Profile  
✅ Admin Dashboard  
✅ User Management  
✅ Product Management  
✅ System Monitoring  
✅ Analytics  

---

## ⚙️ ADMIN CAPABILITIES

From Dashboard, admin can:
- 📊 View system statistics
- 👥 Manage users
- 📦 Manage product listings
- 📋 View system logs
- 📈 See analytics
- 🔔 Manage notifications

---

## ❓ TROUBLESHOOTING

**Server won't start?**
- Check if port 8000 is available
- Verify Python is installed
- Ensure you're in the backend directory

**404 errors?**
- Check if migrations were applied
- Verify URL paths are correct
- Ensure templates exist

**Database locked?**
- Close all Django processes
- Delete `.sqlite3-journal` files
- Try again

---

## 📚 DOCUMENTATION

For more details, read:
- **INTEGRATION_GUIDE.md** - Technical guide
- **USER_GUIDE.md** - User features
- **QUICK_START.md** - Quick reference
- **STRUCTURE.md** - Architecture
- **INTEGRATION_COMPLETE.md** - Full summary
- **PROJECT_COMPLETE.md** - Completion checklist

---

## ✨ QUICK CHECKLIST

Before going live:

- [ ] Server starts without errors
- [ ] Can access http://localhost:8000/
- [ ] Can sign up with new account
- [ ] Can login with credentials
- [ ] Can see navbar on all pages
- [ ] Can click Dashboard as admin
- [ ] Can post products as farmer
- [ ] Can edit profile
- [ ] Can logout
- [ ] Mobile navbar works

---

## 🎉 YOU'RE ALL SET!

**System Status**: ✨ READY TO USE ✨

**Start Command**:
```bash
cd backend && python manage.py runserver 0.0.0.0:8000
```

**Access**: http://localhost:8000/

**Admin**: admin / admin

---

**Questions?** Check the documentation files or review the code in the backend/frontend folders.

**Happy Farming!** 🌾
