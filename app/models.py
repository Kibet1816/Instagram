from django.db import models

# Create your models here.
class Image(models.Model):
    """
    Image model class
    """
    image = models.ImageField(upload_to = 'media/')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True)

    @classmethod
    def all_images(cls):
        images = cls.objects.all()

    
class Profile(models.Model):
    """
    Profile model class
    """
    photo = models.ImageField(upload_to='media/')
    bio = models.TextField()