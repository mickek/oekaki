import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'oekaki'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.stable'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
