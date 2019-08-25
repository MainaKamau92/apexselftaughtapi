from django.db import models

from apexselftaught.apps.authentication.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    secondary_email = models.CharField(max_length=250)
    user_bio = models.TextField()
    avatar = models.URLField()
    country = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    industry = models.CharField(max_length=255)
    github = models.URLField()
    website = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name='user',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
