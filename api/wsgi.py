"""
Vercel serverless function handler for Django application
"""
def handler(request):
import os
import sys
from pathlib import Path

# Attempt to support both local development and Vercel serverless runtime
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = PROJECT_ROOT / 'backend'

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agricultural.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
from asgiref.wsgi import WsgiToAsgi

# WSGI application
_wsgi_app = get_wsgi_application()

# Expose an ASGI-compatible application which many serverless platforms accept
app = WsgiToAsgi(_wsgi_app)

# For Vercel's Python serverless, the module should expose a callable named
# `handler` (or `app`). We export `app` (ASGI) and also provide `handler`
# that forwards to the ASGI app when called synchronously.
async def _asgi_call(scope, receive, send):
    await app(scope, receive, send)

def handler(request):
    """Compatibility handler used by Vercel's Python runtime.

    Vercel's runtime may call this module with a request-like object. If
    their runtime supports ASGI directly it will use `app`. This handler is
    kept as a synchronous adapter to remain compatible with multiple runtimes.
    """
    # If the runtime provides an ASGI gateway, returning the ASGI app works.
    try:
        return app(request)
    except Exception:
        # Fallback: try to call the WSGI app directly
        return _wsgi_app(request.environ, request.start_response)
