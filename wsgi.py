import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'oekaki.settings.stable'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
