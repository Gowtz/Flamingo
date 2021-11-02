from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import BlogModel


@receiver(pre_save, sender=BlogModel)
def removeOldFiles(sender, instance, **kwargs):
    if not instance._state.adding:
        try:
            obj = BlogModel.objects.get(pk=instance.pk)
            new_image = instance.image
            if obj and obj.image.url != new_image.url:
                obj.delete()
        except:
            pass