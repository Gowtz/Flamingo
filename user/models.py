from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='Profile/default.png',
                               upload_to='Profile/images/',
                               blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.avatar.path)

        if image.height > 200 and image.width > 200:
            ouput_size = (200, 200)
            image.thumbnail(ouput_size)
            image.save(self.avatar.path)