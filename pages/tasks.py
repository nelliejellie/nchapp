from celery import group, shared_task
from celery.schedules import crontab
from django.utils import timezone
from datetime import datetime
from .models import Corper_blog, Comment
from django.core.mail import send_mail




#task to filter blog posts
@shared_task(run_every=crontab(minute=('*/5')))
def delete_blog_posts():
    blog_posts = Corper_blog.objects.all()
    for post in blog_posts:
        if post.expiry_date < datetime.now().date():
            print (f'{post} is greater than expiry date')
            post.delete()
    return f'expired post has been deleted at {timezone.now()}'