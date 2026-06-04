"""
Vercel serverless function handler for Django application
"""
import os
import sys
import django

# Add backend directory to path
sys.path.insert(0, '/var/task/backend')

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agricultural.settings')
django.setup()

from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Get Django WSGI application
app = get_wsgi_application()

# Vercel handler
def handler(request):
    return app(request)
