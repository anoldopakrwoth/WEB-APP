import os
import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BACKEND_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agricultural.settings')

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

try:
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception:
    pass
