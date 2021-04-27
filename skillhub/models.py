from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Artisan(models.Model):
    status_choices = (
       ('not selected','not selected'),
       ('Carpenter', 'Carpenter'),
       ('Electrician', 'Electrician'),
       ('Realtor','Realtor'),
       ('Software-developer','Software-developer'),
       ('Personal-Shopper','Personal-Shopper'),
       ('beautician','beautician'),
       ('Hair-dresser','Hair-dresser'),
       ('Barber','Barber'),
       ('Fashion-designer','Fashion-designer'),
       ('Painter','Painter'),
       ('Photographer','Photographer'),
       ('Baker','Baker'),

   )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=30, choices=status_choices,default='not selected')
    descriptions = models.TextField(max_length=200, blank=False)
    contact_number = models.CharField(max_length=13, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    image = CloudinaryField('image')
    image_two = CloudinaryField('image', blank=True)
    image_three = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):  
        return reverse('skill_detail', args=[self.id])

@receiver(pre_delete, sender=Artisan)
def artisan_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
    if instance.image_two.public_id:
        cloudinary.uploader.destroy(instance.image_two.public_id)
    if instance.image_three.public_id:
        cloudinary.uploader.destroy(instance.image_three.public_id)
