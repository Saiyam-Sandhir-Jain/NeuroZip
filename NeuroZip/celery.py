import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NeuroZip.settings')

celery_app = Celery('NeuroZip')

# Load celery settings from settings.py
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover celery tasks from all the apps/microservices
celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")