import os
import sys
from pathlib import Path

# Add the Backend folder to Python's path so Vercel can find 'fooddelivery'
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fooddelivery.settings')
application = get_wsgi_application()

# Vercel requires 'app' variable
app = application
