# 🌾 AgriLink - Agricultural Marketplace

A modern Django web application that connects village farmers directly to town markets. AgriLink enables farmers to post their fresh produce with detailed information and buyers to browse and discover quality agricultural products.

## ✨ Features

- **🏪 Marketplace Feed** - Browse all available agricultural produce listings
- **📋 Product Details** - View comprehensive product information with seller contact details
- **✍️ Post Harvest** - Easy-to-use form for farmers to list their produce
- **📸 Photo Uploads** - Farmers can upload product photos for better visibility
- **🗺️ Location Tracking** - Display origin village and target market town
- **💰 Price Display** - Clear pricing in Uganda Shillings (UGX)
- **👨‍🌾 Seller Information** - Contact details and availability status
- **📱 Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **✨ Modern UI** - Bootstrap 5 with attractive gradients and hover animations

## 🛠️ Tech Stack

- **Backend**: Django 6.0.5
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3
- **Database**: SQLite3
- **Python**: 3.14.5
- **Server**: Django Development Server (local) / WSGI (production)

## 📦 Project Structure

```
Agricultural/
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database
├── README.md                          # This file
├── Agricultural/                      # Project settings folder
│   ├── settings.py                   # Django configuration
│   ├── urls.py                       # URL routing configuration
│   ├── wsgi.py                       # WSGI configuration
│   ├── asgi.py                       # ASGI configuration
│   └── __init__.py
├── marketplace/                       # Main application
│   ├── models.py                     # Database models (ProduceListing)
│   ├── views.py                      # Business logic
│   ├── urls.py                       # App-level URL patterns
│   ├── admin.py                      # Django admin config
│   ├── apps.py                       # App configuration
│   ├── migrations/                   # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_rename_create_at_to_created_at.py
│   │   ├── 0003_alter_producelisting_options_and_more.py
│   │   └── 0004_producelisting_image.py
│   └── templates/marketplace/        # HTML templates
│       ├── feed.html                 # Marketplace homepage
│       ├── detail.html               # Product details page
│       └── create_listing.html       # Produce posting form
└── media/                            # User-uploaded images
    └── listings/                     # Product photos

```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment tool (venv)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "c:\Users\Arnold\OneDrive\Desktop\WEB APP"
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate it
   .\.venv\Scripts\Activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==6.0.5 pillow python-dotenv
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 📖 How to Use

### For Farmers (Sellers)

1. Navigate to the homepage
2. Click **"+ Post Your Harvest"** button
3. Fill in the form:
   - **Produce Name**: e.g., "Fresh Organic Tomatoes"
   - **Price**: Enter price in Uganda Shillings (UGX)
   - **Quantity/Measurement**: e.g., "50kg bag"
   - **Village/Origin**: Where the produce is from
   - **Target Town**: Nearest market town
   - **Description**: Details about quality, freshness, delivery terms
   - **Product Photo** (optional): Upload a clear image of your produce
4. Click **"✓ Publish Listing"** to submit
5. Your listing will appear on the marketplace feed immediately

### For Buyers

1. Visit the **marketplace homepage** to browse all available produce
2. Each product card shows:
   - Product name
   - Price in UGX
   - Origin village and target town
   - Farmer/seller information
3. Click **"View Details"** to see:
   - Complete product information
   - Product photo (if uploaded)
   - Full description
   - Seller contact details
   - Availability status

## 💾 Database Schema

### ProduceListing Model

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| seller | ForeignKey | Link to Django User (farmer) |
| title | CharField | Product name |
| description | TextField | Product details |
| price | DecimalField | Price in UGX |
| quantity | CharField | Amount/measurement |
| image | ImageField | Product photo |
| village_origin | CharField | Origin location |
| target_town | CharField | Destination market |
| created_at | DateTimeField | Listing creation time |
| is_available | BooleanField | Availability status |

## 🎨 Styling & Design

- **Color Scheme**: Green gradients (#2ecc71 to #1a5f3f) for agricultural theme
- **Framework**: Bootstrap 5.3 for responsive layout
- **Features**:
  - Smooth hover animations
  - Gradient backgrounds
  - Card-based layout
  - Emoji icons for better UX
  - Mobile-optimized responsive design

## 🔗 URL Routes

| Route | View | Description |
|-------|------|-------------|
| `/` | market_feed | Marketplace homepage |
| `/listing/<id>/` | listing_detail | Product details page |
| `/listing/new/` | create_listing | Form to post new produce |
| `/admin/` | Django Admin | Admin interface |

## 📝 Media Files

Uploaded product images are stored in:
- **Location**: `media/listings/` directory
- **Served at**: `/media/listings/<filename>`
- **Development**: Automatically served by Django
- **Production**: Configure static/media server (nginx, Apache, etc.)

## ⚙️ Configuration

### Debug Mode
- Currently: `DEBUG = True` (Development)
- For production: Set `DEBUG = False` in `settings.py`

### Allowed Hosts
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']
```

### Database
- SQLite3: `db.sqlite3`
- To reset: Delete `db.sqlite3` and run `python manage.py migrate`

## 🔐 Admin Panel

Access Django admin at: **http://127.0.0.1:8000/admin/**

Manage:
- Produce listings
- User accounts
- Product availability

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS` with your domain
3. Configure static/media file serving
4. Use production WSGI server (Gunicorn, uWSGI)
5. Set up database backup system
6. Enable HTTPS/SSL

## 📱 Responsive Design

The application is fully responsive and tested on:
- ✅ Desktop (1920px and above)
- ✅ Laptop (1024px - 1920px)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (320px - 768px)

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8080
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Migration Issues
```bash
python manage.py migrate --run-syncdb
```

### Image Upload Not Working
Ensure `media/` directory exists and has write permissions:
```bash
mkdir media
mkdir media/listings
```

## 📞 Features Coming Soon

- User authentication & profiles
- Search & filtering functionality
- Direct messaging between farmers and buyers
- Payment integration
- Rating & reviews system
- Bulk order management
- SMS notifications

## 📄 License

This project is for educational and demonstration purposes.

## 👥 Contributing

This is a demo project. For improvements or bug reports, please review the code structure.

## 📧 Support

For issues or questions, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/

---

**🌾 Connecting Farmers to Markets | AgriLink © 2026**
