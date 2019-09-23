from django.db import models

from apexselftaught.apps.authentication.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    secondary_email = models.CharField(max_length=250, null=True)
    user_bio = models.TextField(null=True)
    avatar = models.URLField(null=True)
    country = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, null=True)
    industry = models.CharField(max_length=255, null=True)
    github = models.URLField(null=True)
    website = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name='user',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
