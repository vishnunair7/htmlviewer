import os
import sys

path = '/var/www/slackhtmlviewer'
if path not in sys.path:
    sys.path.insert(0, '/var/www/slackhtmlviewer')

os.environ['DJANGO_SETTINGS_MODULE'] = 'slackhtmlviewer.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()