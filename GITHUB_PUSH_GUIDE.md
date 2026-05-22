# 🚀 GitHub Push Guide for AgriLink

This guide will help you push your AgriLink project to your GitHub account.

## Prerequisites

1. **Git installed** on your computer
   - Download from: https://git-scm.com/download/win
   - Install with default settings
   - Restart your terminal after installation

2. **GitHub account**
   - If you don't have one, create at: https://github.com/signup

3. **GitHub Personal Access Token** (recommended for authentication)
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (full control of private repositories)
   - Copy the token (you'll need it during push)

---

## Step-by-Step Instructions

### 1. Create a New Repository on GitHub

1. Go to https://github.com/new
2. **Repository name**: `agrilink` (or any name you prefer)
3. **Description**: "Agricultural Marketplace - Django Web App connecting farmers to town markets"
4. Choose **Public** or **Private** (your preference)
5. ⚠️ **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **"Create repository"**

### 2. Copy Repository URL

After creation, you'll see a page with your repository URL. Copy it:
- It will look like: `https://github.com/YOUR_USERNAME/agrilink.git`

### 3. Open Terminal in Project Directory

1. Open PowerShell or Command Prompt
2. Navigate to your project:
   ```powershell
   cd "c:\Users\Arnold\OneDrive\Desktop\WEB APP"
   ```

### 4. Initialize Git (if not already done)

```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 5. Add All Files

```powershell
git add .
```

### 6. Create Initial Commit

```powershell
git commit -m "Initial commit: AgriLink agricultural marketplace with Django, Bootstrap 5, image uploads, and UGX currency"
```

### 7. Add Remote Repository

Replace `YOUR_USERNAME` and `REPO_NAME` with your actual GitHub username and repository name:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/agrilink.git
```

Example:
```powershell
git remote add origin https://github.com/arnold/agrilink.git
```

### 8. Rename Branch (if needed)

If you get an error about `master` vs `main`:

```powershell
git branch -M main
```

### 9. Push to GitHub

```powershell
git push -u origin main
```

When prompted for password:
- **Username**: Your GitHub username
- **Password**: Your Personal Access Token (not your password!)

---

## Troubleshooting

### "fatal: not a git repository"
```powershell
# Make sure you're in the correct directory
pwd  # Check current directory
cd "c:\Users\Arnold\OneDrive\Desktop\WEB APP"
git init  # Initialize if needed
```

### "fatal: remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/agrilink.git
```

### Authentication Issues
- Use your **GitHub Personal Access Token** (not your GitHub password)
- Generate token: https://github.com/settings/tokens
- Check "repo" scope when creating token

### Large Files Warning
If you get warnings about large files:
1. The SQLite database might be large
2. It's okay for small databases
3. For production, use PostgreSQL instead

---

## After Pushing to GitHub

1. ✅ Verify on GitHub:
   - Go to your repository: `https://github.com/YOUR_USERNAME/agrilink`
   - See all your files displayed

2. 📋 Update your profile:
   - Add repository to your GitHub profile
   - Add description and topics (django, agriculture, marketplace)

3. 🔗 Share the repository:
   - Share with others: `https://github.com/YOUR_USERNAME/agrilink`
   - Include in your portfolio

4. 📝 Optional - Add GitHub Pages:
   - Go to Settings → Pages
   - Select main branch as source
   - View your site at: `https://YOUR_USERNAME.github.io/agrilink`

---

## Commands Cheat Sheet

```powershell
# Check git status
git status

# See commit history
git log

# Make changes and push updates
git add .
git commit -m "Your commit message"
git push

# Check remote URL
git remote -v

# Clone repository locally (for others)
git clone https://github.com/YOUR_USERNAME/agrilink.git
```

---

## Future Updates

After initial push, to update your repository:

```powershell
# Make your changes to files

# Stage changes
git add .

# Commit
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## 📚 Additional Resources

- **Git Guide**: https://guides.github.com/
- **GitHub Docs**: https://docs.github.com/
- **Django Deployment**: https://docs.djangoproject.com/en/6.0/howto/deployment/
- **GitHub Profile**: https://github.com/settings/profile

---

## ⚠️ Important Security Notes

1. **Never commit secrets**:
   - API keys
   - Database credentials
   - Secret keys
   - Use `.env` file with `.gitignore`

2. **Update `settings.py` for production**:
   ```python
   DEBUG = False
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

3. **Current `settings.py` is for development only**
   - Change before production deployment

---

**Good luck pushing your project! 🚀**
