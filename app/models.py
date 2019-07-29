from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Profile model class
    """
    photo = models.ImageField(upload_to='media/')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)


class Image(models.Model):
    """
    Image model class
    """
    image = models.ImageField(upload_to = 'media/')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    likes = models.IntegerField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def save_image(self):
        return self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()

        return images