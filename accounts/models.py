from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class MyUser(AbstractUser):
    reg_no = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=10, blank=True)
    local_govt = models.CharField(max_length=30, blank=True)
    created =  models.DateField(default=datetime.now, db_index=True, blank=True)
    expiry_date = models.DateField(null=True)


@receiver(post_save, sender=MyUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
