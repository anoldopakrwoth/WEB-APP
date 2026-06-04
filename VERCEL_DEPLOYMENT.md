# Vercel Deployment Guide - Agricultural Web App

Complete step-by-step guide to deploy your Django app on Vercel with serverless functions.

---

## ✅ Pre-Deployment Checklist

- [ ] Django app runs locally (`python manage.py runserver`)
- [ ] All migrations applied (`python manage.py migrate`)
- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] `requirements.txt` updated with all dependencies
- [ ] `.env` file created with all environment variables
- [ ] `vercel.json` exists in project root
- [ ] GitHub repository is public or connected to Vercel

---

## 🚀 Step 1: Install Vercel CLI

### Option A: Using npm
```bash
npm i -g vercel
```

### Option B: Using Homebrew (macOS)
```bash
brew install vercel
```

### Verify Installation
```bash
vercel --version
```

---

## 🔧 Step 2: Create `vercel.json` Configuration

Your project already has `vercel.json` configured. Verify it contains:

```json
{
  "buildCommand": "cd backend && pip install -r requirements.txt && python manage.py collectstatic --noinput",
  "outputDirectory": "backend",
  "env": {
    "DJANGO_SETTINGS_MODULE": "Agricultural.settings",
    "PYTHONPATH": "/var/task"
  },
  "functions": {
    "backend/wsgi.py": {
      "runtime": "python3.11",
      "memory": 1024,
      "maxDuration": 60
    }
  }
}
```

---

## 📦 Step 3: Update `requirements.txt`

Ensure your `backend/requirements.txt` includes:

```
Django==6.0.5
Pillow==12.2.0
psycopg2-binary==2.9.12
gunicorn==26.0.0
WhiteNoise==6.12.0
dj-database-url==3.1.2
python-dotenv==1.0.1
requests==2.32.3
```

Update it:
```bash
cd backend
pip freeze > requirements.txt
```

---

## 🔐 Step 4: Create Production Environment Variables

### Generate Secure SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Create `.env.production` (for reference only - don't commit)

```ini
DEBUG=False
SECRET_KEY=<your-generated-key>
ALLOWED_HOSTS=your-domain.vercel.app,www.your-domain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
CSRF_TRUSTED_ORIGINS=https://your-domain.vercel.app,https://www.your-domain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## 📤 Step 5: Push to GitHub

```bash
git add .
git commit -m "Deploy: Production-ready configuration for Vercel"
git push origin main
```

---

## 🌐 Step 6: Deploy with Vercel CLI

### First Time Deployment

```bash
vercel --prod
```

**Follow prompts:**
1. Link to existing project or create new
2. Select scope (personal or organization)
3. Select Django app directory
4. Configure build settings (default OK)

### Subsequent Deployments

```bash
vercel --prod
```

---

## 🔗 Step 7: Connect GitHub for Auto-Deploy

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click **"New Project"**
3. Import your GitHub repository
4. Configure:
   - **Build Command:** `cd backend && pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Output Directory:** `backend`
   - **Install Command:** `pip install -r backend/requirements.txt`
5. Add Environment Variables (see Step 4)
6. Click **"Deploy"**

Now every push to `main` automatically deploys! 🚀

---

## 🔑 Step 8: Configure Environment Variables in Vercel Dashboard

1. Go to **Project Settings** → **Environment Variables**
2. Add each variable from `.env.production`:
   - `DEBUG` = `False`
   - `SECRET_KEY` = `your-secret-key`
   - `ALLOWED_HOSTS` = `your-domain.vercel.app`
   - `DATABASE_URL` = `postgresql://...`
   - `CSRF_TRUSTED_ORIGINS` = `https://your-domain.vercel.app`
   - `SECURE_SSL_REDIRECT` = `True`
   - `SESSION_COOKIE_SECURE` = `True`
   - `CSRF_COOKIE_SECURE` = `True`

3. Set environment to **Production**

---

## 🗄️ Step 9: Database Setup

### Option A: Using Render PostgreSQL (Recommended)

1. Go to [render.com](https://render.com)
2. Create free PostgreSQL database
3. Copy connection string
4. Add to Vercel env var: `DATABASE_URL=<connection-string>`

### Option B: Using AWS RDS

1. Create RDS PostgreSQL instance
2. Allow Vercel IP ranges (0.0.0.0/0 for development)
3. Add connection string to Vercel env vars

### Option C: Using Vercel PostgreSQL (Beta)

```bash
vercel postgres create
# Get connection string and add to env vars
```

---

## 📝 Step 10: Run Migrations in Production

After first deployment:

```bash
# Via Vercel dashboard - Deployments tab
# Look for migration output in build logs

# Or manually via CLI
vercel exec python backend/manage.py migrate
```

Or add to `vercel.json` build step:

```json
{
  "buildCommand": "cd backend && python manage.py migrate && python manage.py collectstatic --noinput"
}
```

---

## 🎯 Step 11: Custom Domain Setup

### Using Vercel DNS (Easiest)

1. Go to **Project Settings** → **Domains**
2. Enter your domain (e.g., `yourdomain.com`)
3. Click **"Add"**
4. Follow Vercel's DNS setup instructions
5. Wait 24-48 hours for propagation

### Using External DNS Provider

1. Go to **Project Settings** → **Domains**
2. Add domain manually
3. Add DNS records provided by Vercel:
   - **A Record:** `76.76.19.0`
   - **CNAME:** `www` → `cname.vercel-dns.com`

---

## 🔒 Step 12: SSL/TLS Certificate

Vercel **automatically** provides free SSL certificates via Let's Encrypt.

**Verify:**
1. Go to **Project Settings** → **SSL/TLS**
2. Confirm certificate is active
3. Test: `https://yourdomain.com`

---

## 🧪 Step 13: Test Production Deployment

### Check Deployment Status
```bash
vercel logs --prod
```

### Test Your App
```bash
curl https://yourdomain.com
# Should return HTML of your site

curl https://yourdomain.com/admin
# Should return 200 if admin page loads
```

### Access Admin Panel
```
https://yourdomain.com/admin
```

### Check Static Files
```
https://yourdomain.com/static/css/style.css
# Should load correctly
```

---

## 📊 Step 14: Monitoring & Logging

### View Logs
```bash
# Real-time logs
vercel logs --prod --follow

# Function logs
vercel logs --prod --function=wsgi
```

### Monitor Performance
1. Dashboard → **Analytics**
2. View:
   - Response times
   - Error rates
   - CPU usage
   - Memory usage

### Set Up Alerts
1. **Project Settings** → **Alerts**
2. Configure notifications for:
   - Deployment failures
   - Performance issues
   - Error rates > threshold

---

## 🚨 Troubleshooting

### Build Fails: "No such file or directory: manage.py"

**Fix:** Verify `vercel.json` paths:
```json
{
  "buildCommand": "cd backend && pip install -r requirements.txt && python manage.py collectstatic --noinput"
}
```

### 502 Bad Gateway Error

**Cause:** Django settings error or database connection issue

**Fix:**
```bash
# Check logs
vercel logs --prod

# Verify environment variables
vercel env list

# Ensure SECRET_KEY is set
# Ensure DATABASE_URL is correct
```

### Static Files Return 404

**Fix:** Ensure WhiteNoise is enabled in `settings.py`
```python
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this first
    'django.middleware.security.SecurityMiddleware',
    # ... rest of middleware
]
```

### Database Connection Refused

**Cause:** Database URL incorrect or firewall blocked

**Fix:**
- Verify `DATABASE_URL` in Vercel dashboard
- Check database firewall allows Vercel IPs
- Test connection locally first

### Environment Variables Not Loading

**Fix:**
```bash
# Redeploy to load new env vars
vercel --prod

# Or manually trigger rebuild
vercel deploy --prod --force
```

---

## 📈 Performance Optimization

### Enable Caching for Static Files

Already configured in `vercel.json`:
```json
{
  "routes": [
    {
      "src": "/static/(.*)",
      "headers": {
        "Cache-Control": "public, max-age=31536000, immutable"
      }
    }
  ]
}
```

### Use CDN for Media Files

Configure CloudFront or Vercel Edge Network for optimal global delivery.

### Optimize Images

```python
from PIL import Image
img = Image.open('image.jpg')
img.save('optimized.jpg', optimize=True, quality=85)
```

---

## 🔄 Continuous Integration/Deployment

### Auto-Deployment on Git Push

Already configured when you:
1. Connected GitHub repository
2. Set environment variables in Vercel dashboard
3. Have valid `vercel.json`

### Manual Deployment

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# Redeploy specific commit
vercel --prod <commit-sha>
```

---

## 📞 Useful Commands

```bash
# List all projects
vercel projects ls

# Show project info
vercel projects info

# View deployment history
vercel list

# Inspect specific deployment
vercel inspect <deployment-id>

# View environment variables
vercel env list

# Add env variable
vercel env add SECRET_KEY

# Remove env variable
vercel env remove SECRET_KEY

# Promote preview to production
vercel promote <preview-deployment-url>
```

---

## ✅ Post-Deployment Checklist

- [ ] Site loads on custom domain
- [ ] Admin panel accessible (`/admin`)
- [ ] Static files load correctly
- [ ] Database queries working
- [ ] HTTPS/SSL certificate valid
- [ ] Environment variables correct
- [ ] Logs show no errors
- [ ] Performance metrics acceptable
- [ ] Email notifications working (if configured)
- [ ] Database backups scheduled

---

## 🎯 Production Best Practices

1. **Regular Backups**
   ```bash
   # Database backup
   DATABASE_URL=<url> pg_dump > backup.sql
   ```

2. **Monitor Error Rates**
   - Check Sentry or error tracking service
   - Set up alerts for critical errors

3. **Security Updates**
   - Keep Django updated
   - Review security advisories
   - Update dependencies monthly

4. **Performance Monitoring**
   - Track response times
   - Monitor memory usage
   - Analyze slow queries

5. **Version Control**
   - Tag production releases
   - Keep changelog updated
   - Document deployment process

---

## 📚 Additional Resources

- [Vercel Django Documentation](https://vercel.com/docs/concepts/functions/serverless-functions/python)
- [Django Production Deployment](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Vercel CLI Documentation](https://vercel.com/docs/cli)
- [PostgreSQL on Render](https://render.com/docs/databases)
- [Django Security Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

---

## 🚀 Success!

Your Django agricultural marketplace is now live in production on Vercel with:
- ✅ Auto-scaling serverless functions
- ✅ Global CDN for fast content delivery
- ✅ Free SSL/TLS encryption
- ✅ Automatic deployments from GitHub
- ✅ Environment-based configuration
- ✅ Production PostgreSQL database

**Monitor your deployment regularly and keep dependencies updated!**

*Deployment Guide Last Updated: 2026-06-04*
