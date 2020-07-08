from django.db.models.signals import post_save
from django.dispatch import receiver
from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.core.send_email import send_confirmation_email
from apexselftaught.apps.profiles.models import Profile


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if instance and created:
        print("I gets called >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        instance.profile = Profile.objects.create(user=instance)
        send_confirmation_email(instance)
