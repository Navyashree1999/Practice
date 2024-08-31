from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','demoproject.settings')
app = Celery('demoproject',  broker='redis://127.0.0.1:6379')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings')
app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'demoapp.tasks.send_mail_task',
        'schedule': 30.0,  # every 30 seconds it will be called
        # 'args': (2,)  # you can pass arguments also if required
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
