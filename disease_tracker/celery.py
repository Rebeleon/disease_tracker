from celery import Celery

app = Celery('your_app_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
