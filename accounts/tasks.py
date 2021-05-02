from celery import group, shared_task
from celery.schedules import crontab
from django.utils import timezone
from datetime import datetime
from .models import MyUser
from django.core.mail import send_mail




#task to filter blog posts
@shared_task(run_every=crontab(minute=('*/5')))
def delete_user():
    user = MyUser.objects.all()
    for users in user:
        if users.expiry_date < datetime.now().date():
            print (f'{user} is n longer a corper')
            users.delete()
    return f'former corpers account has been deleted has been deleted at {timezone.now()}'