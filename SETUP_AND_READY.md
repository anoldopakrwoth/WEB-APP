# Agricultural Web App - Setup & Installation Guide

Your Django agricultural marketplace is now fully fixed and ready to use! 🎉

## ✅ What's Been Fixed

### Database
- ✅ Applied all pending migrations (marketplace.0006_producelisting_video)
- ✅ Database fully synchronized

### Code Quality
- ✅ All imports verified and working
- ✅ All models properly configured
- ✅ All views syntax validated
- ✅ Static files collected and optimized

### Production Configuration
- ✅ Comprehensive logging system configured
- ✅ Security headers implemented (CSP, X-Frame-Options, etc.)
- ✅ HTTPS/SSL ready for production
- ✅ HSTS preload configuration
- ✅ CSRF and Session cookie security hardened

### Deployment Ready
- ✅ Vercel deployment configuration
- ✅ Render deployment support
- ✅ Environment-based security settings

---

## 🚀 Quick Start - Local Development

### Prerequisites
- **Python 3.10+**
- **pip** (Python package manager)
- **Virtual Environment** support

### 1. **Clone Repository & Navigate**
```bash
git clone https://github.com/anoldopakrwoth/WEB-APP.git
cd WEB-APP
```

### 2. **Create & Activate Virtual Environment**

**Windows (PowerShell):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. **Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

### 4. **Set Environment Variables**
Create `backend/.env`:
```
DEBUG=True
SECRET_KEY=your-development-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. **Run Migrations**
```bash
python manage.py migrate
```

### 6. **Create Superuser (Admin)**
```bash
python manage.py createsuperuser
```

### 7. **Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

### 8. **Run Development Server**
```bash
python manage.py runserver
```

The server will be available at: **http://localhost:8000**
Admin panel: **http://localhost:8000/admin**

---

## 📁 Project Structure

```
WEB-APP/
├── backend/                    # Django backend
│   ├── Agricultural/          # Main project settings
│   │   ├── settings.py        # Django configuration ✅ FIXED
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── accounts/              # User authentication
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── marketplace/           # Product listings
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── dashboard/             # Admin dashboard
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── common/                # Shared utilities
│   │   ├── utils.py           # Helper functions
│   │   └── validators.py      # File validators ✅
│   ├── manage.py
│   ├── requirements.txt       # Python dependencies
│   └── db.sqlite3             # Database ✅ MIGRATED
│
├── frontend/                   # Static files & templates
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, JS, images
│   └── media/                 # User uploads
│
├── staticfiles/               # Collected static files
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── vercel.json                # Vercel deployment config
├── SETUP_AND_READY.md         # This file
├── VERCEL_DEPLOYMENT.md       # Vercel setup guide
└── README.md                  # Main project README
```

---

## 🔒 Security Features

Your app includes enterprise-grade security:
- **HTTPS/SSL Support** - Ready for production
- **CSRF Protection** - Secure form submissions
- **Session Security** - Secure cookies with HttpOnly flag
- **Content Security Policy** - Prevents XSS attacks
- **Security Headers** - X-Frame-Options, X-Content-Type-Options
- **HSTS** - HTTP Strict Transport Security
- **SQL Injection Prevention** - Django ORM protection
- **Environment-based Configuration** - Secrets never in code

---

## 📦 Key Dependencies

- **Django 6.0.5** - Web framework
- **Pillow 12.2.0** - Image processing
- **psycopg2-binary 2.9.12** - PostgreSQL support
- **gunicorn 26.0.0** - Production WSGI server
- **WhiteNoise 6.12.0** - Static files serving
- **dj-database-url 3.1.2** - Database configuration
- **python-dotenv** - Environment variable management

See `backend/requirements.txt` for the complete list.

---

## 🗄️ Database Configuration

### Local Development
Uses **SQLite** (`db.sqlite3`) for simplicity - no additional setup needed.

### Production
Set the `DATABASE_URL` environment variable:
```
# PostgreSQL (Recommended)
DATABASE_URL=postgresql://user:password@host:5432/database_name

# MySQL
DATABASE_URL=mysql://user:password@host:3306/database_name
```

**Supported Databases:**
- PostgreSQL (recommended for production)
- MySQL 5.7+
- SQLite (development only)
- MariaDB

---

## 📝 Common Django Commands

```bash
# Create new migration after model changes
python manage.py makemigrations

# Apply pending migrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Collect all static files
python manage.py collectstatic --noinput

# Run automated tests
python manage.py test

# Django interactive shell
python manage.py shell

# Check for configuration issues
python manage.py check
python manage.py check --deploy

# Load sample data
python manage.py loaddata initial_data.json

# Backup database
python manage.py dumpdata > backup.json
```

---

## 🌍 Deployment Options

### **Option 1: Vercel (Recommended for Serverless)**
✅ **Best for:** Scalable, low-maintenance deployments

See **[VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)** for detailed setup

**Features:**
- Serverless functions (auto-scaling)
- Global CDN with edge caching
- Free SSL/TLS certificates
- Environment variable management
- Automatic deployments from GitHub
- Analytics & monitoring

**Quick Deploy:**
```bash
npm i -g vercel
vercel --prod
```

### **Option 2: Render**
✅ **Best for:** Traditional app hosting

**Features:**
- Native Django support
- PostgreSQL included
- Automatic SSL
- Environment management
- GitHub auto-deploy

**Setup:** Create account at render.com and connect GitHub repo

### **Option 3: PythonAnywhere**
✅ **Best for:** Simplicity

**Features:**
- Django pre-configured
- PostgreSQL support
- Web-based file editor
- No server management

### **Option 4: DigitalOcean / Linode**
✅ **Best for:** Full control

**Features:**
- VPS with full SSH access
- Docker support
- Managed databases
- Starting at $4/month

---

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Check for configuration errors
python manage.py check

# Apply any pending migrations
python manage.py migrate

# Verify all dependencies installed
pip install -r requirements.txt
```

### Static Files Not Loading
```bash
# Clear and recollect static files
python manage.py collectstatic --clear --noinput

# Check WhiteNoise is enabled in settings.py
# It should be first in MIDDLEWARE
```

### Database Errors
```bash
# Reset migrations (development only - CAUTION!)
python manage.py migrate --fake-initial

# Or reset specific app
python manage.py migrate accounts zero
python manage.py migrate accounts
```

### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8001

# Or find and kill process on port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :8000   # Windows
```

### Permission Denied on Media Files
```bash
# Ensure proper permissions
chmod -R 755 media/
chmod -R 755 staticfiles/
```

### Import Errors
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Verify Django version
python -c "import django; print(django.get_version())"
```

---

## 🧪 Testing & Validation

### Pre-Deployment Checklist
```bash
# Run security checks
python manage.py check --deploy

# Run tests
python manage.py test

# Check static files
python manage.py collectstatic --dry-run

# Verify database migrations
python manage.py showmigrations
```

### Load Testing Locally
```bash
# Use Apache Bench
ab -n 100 -c 10 http://localhost:8000/

# Or use locust for detailed reports
pip install locust
locust
```

---

## 🔑 Environment Variables Reference

Create `.env` file in `backend/` directory:

```ini
# Django Settings
DEBUG=False
SECRET_KEY=generate-a-secure-random-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# Email (Optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# AWS S3 (Optional - for media storage)
USE_S3=True
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket

# Logging
LOG_LEVEL=INFO
```

**To generate a secure SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📚 Additional Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Vercel Python Deployment](https://vercel.com/docs/concepts/functions/serverless-functions/python)
- [12 Factor App Methodology](https://12factor.net/)

---

## ✨ Features Ready to Use

- ✅ User Registration & Login with email verification
- ✅ Profile Management with avatar upload
- ✅ Product Listings with Images & Videos
- ✅ Marketplace Feed with search & filtering
- ✅ Admin Dashboard with analytics
- ✅ System Monitoring & logging
- ✅ Email Notifications
- ✅ Security & CORS configuration
- ✅ Error handling & 404/500 pages
- ✅ Pagination & performance optimization

---

## 🎯 Next Steps

1. **Local Testing:**
   ```bash
   python manage.py runserver
   # Visit http://localhost:8000
   ```

2. **Create Test Data:**
   - Access admin panel: http://localhost:8000/admin
   - Create sample products & users

3. **Verify Deployment Config:**
   - Review `vercel.json` settings
   - Check environment variables
   - Test static file collection

4. **Deploy to Production:**
   - Follow [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)
   - Or use alternative platform from above options

5. **Monitor After Deploy:**
   - Check error logs regularly
   - Monitor database queries
   - Set up alerts for critical errors
   - Track performance metrics

---

## 📞 Support & Issues

- **Django Issues:** Check [Django GitHub Issues](https://github.com/django/django/issues)
- **Deployment Issues:** Consult platform-specific documentation
- **Security Concerns:** Review [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## 🚀 You're Production Ready!

Your agricultural marketplace application is fully configured and ready for deployment. Follow the deployment guide for your chosen platform and monitor your application's health in production.

**Happy deploying!** 🎉

*Last Updated: 2026-06-04*
