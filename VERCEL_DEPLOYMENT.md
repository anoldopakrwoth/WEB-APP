# Vercel Deployment Guide

Your project is now configured for Vercel deployment! Follow these steps:

## Step 1: Prerequisites
- Vercel account (https://vercel.com)
- Git repository pushed to GitHub
- Vercel CLI installed: `npm i -g vercel`

## Step 2: Set Up Environment Variables

Add these environment variables in your Vercel Dashboard (`Settings > Environment Variables`):

### Required Variables:
```
DEBUG=False
ALLOWED_HOSTS=*.vercel.app,your-domain.com
SECRET_KEY=<generate-a-new-secure-key>
VERCEL=true
```

### Database Configuration:
```
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>
```

For PostgreSQL, you can use:
- **Neon** (https://neon.tech) - Free PostgreSQL hosting
- **Supabase** (https://supabase.com) - PostgreSQL + extras
- **AWS RDS**
- **DigitalOcean Managed Databases**

### Security Variables:
```
SECURE_SSL_REDIRECT=true
SESSION_COOKIE_SECURE=true
CSRF_COOKIE_SECURE=true
```

### Optional - Static Files (if using S3):
```
AWS_STORAGE_BUCKET_NAME=<bucket-name>
AWS_S3_ACCESS_KEY_ID=<access-key>
AWS_S3_SECRET_ACCESS_KEY=<secret-key>
AWS_S3_REGION_NAME=us-east-1
```

## Step 3: Deploy to Vercel

### Option A: Via Web Dashboard
1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Import your GitHub repository
4. Select root directory (leave default)
5. Add environment variables
6. Click "Deploy"

### Option B: Via CLI
```bash
# Connect to Vercel
vercel login

# Deploy
vercel --prod

# Add environment variables
vercel env add DATABASE_URL
vercel env add SECRET_KEY
vercel env add ALLOWED_HOSTS
# ... add other variables
```

## Step 4: Database Migrations

After first deployment, run migrations:

```bash
vercel env pull  # Download env variables
cd backend
python manage.py migrate
```

Or run via API:
```bash
curl -X POST https://your-project.vercel.app/admin/migrate
```

## Important Notes:

### Static Files
- Static files are collected during build
- WhiteNoise middleware serves them automatically
- Configure CDN in Vercel settings for better performance

### Media Files (Uploads)
- Vercel's filesystem is **ephemeral** (temporary)
- For persistent file storage, use:
  - **Amazon S3**
  - **Cloudinary**
  - **Supabase Storage**
  - **Azure Blob Storage**

### Database Backups
- Ensure your database provider has backups enabled
- Consider using a managed PostgreSQL service

### Logs & Monitoring
- View logs in Vercel Dashboard → Project → Logs
- Monitor using Vercel Analytics (Settings → Analytics)

### Troubleshooting

**Error: "Module not found"**
```bash
# Ensure requirements.txt is in backend directory
# Check vercel.json buildCommand
```

**Error: "Static files not found"**
```bash
# Run locally: python manage.py collectstatic
# Check STATIC_ROOT and STATICFILES_DIRS
```

**Error: "Database connection failed"**
```bash
# Verify DATABASE_URL format
# Check firewall rules allow Vercel IPs
```

## Rollback
```bash
vercel rollback
```

## Local Testing
```bash
# Test Vercel build locally
vercel build

# Test production locally
vercel start
```

## Next Steps
1. ✅ Commit configuration files to Git
2. ✅ Push to GitHub: `git push`
3. ✅ Deploy to Vercel
4. ✅ Configure domain (Settings > Domains)
5. ✅ Set up SSL certificate (automatic with custom domain)
