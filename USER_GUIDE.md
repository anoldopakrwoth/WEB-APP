# 🚀 User Interface - Quick Reference Guide

## 🎯 Getting Started

### **Step 1: Access the Platform**
Visit: **http://localhost:8000/**

### **Step 2: What You'll See**
- 🌾 AgriLink marketplace logo at the top
- Navigation bar with links
- All available product listings
- Call-to-action buttons

---

## 📍 Navigation Links

### **For First-Time Visitors (Not Logged In)**

| Link | Location | Action |
|------|----------|--------|
| 🏠 **Marketplace** | Top navbar | Browse all products |
| 🔐 **Login** | Top right navbar | Sign in with existing account |
| 👥 **Sign Up** | Top right navbar | Create new account |

### **After You Log In (All Users)**

| Link | Location | Action |
|------|----------|--------|
| 🏠 **Marketplace** | Top navbar | Back to home/products |
| 📝 **Post Harvest** | Top navbar | Create new product listing |
| 👤 **User Menu** | Top right navbar | Click your username to see: |
|  | ↳ **Profile** | Edit your information |
|  | ↳ **Logout** | Sign out of account |

### **Extra: If You're the Admin**

| Link | Location | Action |
|------|----------|--------|
| 📊 **Dashboard** | Top navbar | Go to admin panel |
| ✅ Admin credentials | - | Username: `admin` Password: `admin` |

---

## 🔄 Common User Flows

### **Flow 1: Browse Products (Anyone)**
```
1. Visit http://localhost:8000/
2. See all available products
3. Click any product → View full details
4. See seller info and contact
5. Go back → Marketplace link at top
```

### **Flow 2: Create an Account (New User)**
```
1. Click "Sign Up" (top right)
2. Choose role: Farmer or Buyer
3. Enter your information
4. Choose location/village
5. Set password
6. Submit form
7. You'll see: "Account created! Please log in"
8. Click "Login here" link
9. Enter credentials
10. ✓ You're now signed in!
```

### **Flow 3: Log In (Existing User)**
```
1. Click "Login" (top right)
2. Enter username
3. Enter password
4. Click "Login"
5. ✓ Redirected to marketplace
6. See your name in top right
```

### **Flow 4: Post a Product (Farmers)**
```
1. Make sure you're logged in
2. Click "📝 Post Harvest" (top navbar)
3. Fill in product details:
   - Product name
   - Price (UGX)
   - Quantity
   - Village origin
   - Target town
   - Description
4. Optional: Upload product photo
5. Click "Publish Listing"
6. ✓ Your product is now on marketplace
```

### **Flow 5: Edit Your Profile (All Users)**
```
1. Click your username (top right)
2. Click "Profile"
3. Update any information:
   - Name
   - Email
   - Phone
   - Address
   - Village
4. Upload profile picture (optional)
5. Click "Save Changes"
6. ✓ Profile updated!
```

### **Flow 6: Access Admin Dashboard (Admin Only)**
```
1. Login as admin (admin/admin)
2. Click "📊 Dashboard" (top navbar)
3. You'll see admin overview:
   - Dashboard Home
   - User Management
   - Listing Management
   - System Logs
   - Analytics
   - Notifications
```

---

## 🔑 Important URLs

| Page | URL | Who Can Access |
|------|-----|---|
| Marketplace Home | `/` | Everyone |
| Login | `/accounts/login/` | Not logged in users |
| Sign Up | `/accounts/signup/` | Not logged in users |
| Profile | `/accounts/profile/` | Logged in users |
| Product Details | `/marketplace/listing/<id>/` | Everyone |
| Create Listing | `/marketplace/listing/new/` | Logged in users |
| Dashboard | `/dashboard/` | Admin only |

---

## 👥 User Roles & Access

### **🌍 Unauthenticated User (Not Logged In)**
✅ Can:
- Browse marketplace
- View product listings
- See seller details
- Sign up
- Log in

❌ Cannot:
- Post listings
- Edit profile
- Access dashboard

### **👨‍🌾 Farmer (Logged In)**
✅ Can:
- Everything unauthenticated users can do
- Post harvest listings
- Upload product photos
- Edit profile
- View their own listings

❌ Cannot:
- Access admin dashboard

### **👤 Buyer (Logged In)**
✅ Can:
- Everything unauthenticated users can do
- View their profile
- Browse and contact sellers

❌ Cannot:
- Post listings
- Access admin dashboard

### **👨‍💼 Admin (Logged In as admin)**
✅ Can:
- Everything above
- Access full dashboard
- View all users
- Manage listings
- View system logs
- See analytics
- Manage notifications

---

## 🎨 Design Features

### **Navbar (Top of Every Page)**
- **Left**: AgriLink logo (click to go home)
- **Center**: Navigation links (Marketplace, Post Harvest, etc.)
- **Right**: Login/Signup OR User menu

### **Colors**
- 🟢 Green (#2ecc71) - Primary action buttons
- ⚫ Dark (#2c3e50) - Text and headers
- ⚪ White - Cards and backgrounds
- 🔵 Blue - Secondary elements

### **Layout**
- Responsive (works on phone, tablet, desktop)
- Clean cards for products
- Easy-to-read forms
- Large buttons for mobile users

---

## ⚠️ Important Notes

### **Credentials**
- **Admin Username**: `admin`
- **Admin Password**: `admin`
- ⚠️ Change in production!

### **Image Upload**
- Optional for products
- Supported formats: JPG, PNG, GIF
- Shows beautiful preview on product page

### **Password Requirements**
- Minimum 6 characters
- Must match confirmation
- Case-sensitive

### **Location Fields**
- Village/Town helps match supply with demand
- Important for logistics

---

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Can't see "Post Harvest" | You need to be logged in first |
| Can't access Dashboard | Only admin can access it (login as admin) |
| Forgot password | Create new account (password reset coming soon) |
| Product won't upload | Make sure you filled all required fields (*) |
| Can't see my profile | Click your username in top right corner |

---

## 📱 Mobile Tips

- Tap the **hamburger menu** (☰) to collapse/expand navigation
- **Images scale** to fit your screen
- **Forms** are easy to fill on mobile
- **Buttons** are large and touch-friendly

---

## 🔐 Safety Tips

- ✅ Don't share your password
- ✅ Always use strong passwords
- ✅ Log out when done (especially on shared computers)
- ✅ Check seller email before contacting
- ✅ Verify product details before committing

---

## ✨ Features at a Glance

| Feature | Status |
|---------|--------|
| Browse marketplace | ✅ Live |
| Sign up | ✅ Live |
| Log in | ✅ Live |
| Post products | ✅ Live |
| Upload images | ✅ Live |
| Edit profile | ✅ Live |
| Admin dashboard | ✅ Live |
| User management | ✅ Live |
| Listing management | ✅ Live |
| Analytics | ✅ Live |
| System logs | ✅ Live |
| Notifications | ✅ Live |

---

## 🎯 Next Steps

1. **Create your account** → Click "Sign Up"
2. **Browse products** → See what's available
3. **Post your harvest** (farmers) → Click "Post Harvest"
4. **Access dashboard** (admin) → Click "Dashboard"
5. **Explore features** → Try all the links!

---

**🚀 You're all set! Start using AgriLink today!**

For technical details, see: **INTEGRATION_GUIDE.md**
