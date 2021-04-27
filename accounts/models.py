from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    reg_no = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=10, blank=True)
    local_govt = models.CharField(max_length=30, blank=True)
