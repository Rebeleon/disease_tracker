import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disease_tracker.settings')
app = Celery('disease_tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
