from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue, Exchange
from website.constants import CustomerVolume, JobExecutionSpeed


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vanderval.settings')

app = Celery('vanderval')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()