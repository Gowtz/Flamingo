import os
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class BlogModel(models.Model):
    # slug            = models.SlugField(unique=True, blank=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='Blog/')
    create_date     = models.DateField(auto_now_add=True)
    update_date     = models.DateField(auto_now=True)
    content         = models.TextField()


    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.content


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = _get_unique_slug(self, model_name=BlogModel)
    #     super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        try:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        except:
            pass
        super().delete(*args,**kwargs)
