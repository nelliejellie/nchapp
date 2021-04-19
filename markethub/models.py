from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver


# Create your models here.
class Product(models.Model):
    status_choices = (
       ('not selected','not selected'),
       ('Electronics', 'Elecronics'),
       ('Furniture', 'Furniture'),
       ('Apartment','Apartment'),
       ('Other stuffs','Other stuffs'),
   )
    name = models.CharField(max_length=20)
    categories = models.CharField(max_length=30, choices=status_choices,default='not selected')
    sold = models.BooleanField(default=False, blank=True)
    descriptions = models.TextField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    image = CloudinaryField('image')
    image_two = CloudinaryField('image', blank=True)
    image_three = CloudinaryField('image', blank=True)


    def __str__(self):
        return self.name

@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

