from django.db.models.signals import post_save
from django.dispatch import receiver
from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.profiles.models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    email = instance.email
    at_index = email.find("@")
    if not created:
        return
    Profile.objects.create(first_name=email[:at_index], user=instance)
    post_save.disconnect(create_profile, sender=User)
