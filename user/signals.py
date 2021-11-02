from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=Profile)
def delete_old_image_onupdate(sender, instance, **kwargs ):
    try:
        old_avatar = Profile.objects.get(id=instance.id).avatar
    except:
        return
    else:
        try:
            new_avatar = instance.avatar
            if old_avatar and old_avatar.url != new_avatar.url and old_avatar !='Profile/default.png':
                old_avatar.delete(save=False)
        except:
            old_avatar.url = 'Profile/default.png'


@receiver(pre_delete, sender=Profile)
def delete_avatar(sender, instance, **kwargs):
    try:
        instance.avatar.delete(save=False)
    except:
        pass