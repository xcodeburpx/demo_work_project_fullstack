from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# Load settings to script
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dj_backend_server.settings')

# Initialize Celery app
app = Celery('dj_backend_server')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# First debug task
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))