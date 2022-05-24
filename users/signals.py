from django.dispatch import receiver
from django.db.models.signals import post_save
from user_library.models import Profile

from django.contrib.auth.models import User

@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
