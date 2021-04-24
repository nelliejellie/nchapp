import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nchapp.settings')

celery_app = Celery('nchapp')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()