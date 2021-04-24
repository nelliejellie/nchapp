from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver


# Create your models here.
class Corper_blog(models.Model):
    status_choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=datetime.now, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status_choices,default='draft')
    post_image = CloudinaryField('image', blank=False)
    expiry_date = models.DateField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):  
        return reverse('blog_detail', args=[self.id, self.slug])
    
    class Meta():
        ordering = ('-publish',)

@receiver(pre_delete, sender=Corper_blog)
def product_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.post_image.public_id)


class Comment(models.Model):
    post = models.ForeignKey(Corper_blog, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta():
        ordering = ('created',)

    def __str__(self):
        return f'comment by {self.author.username} on {self.post}'