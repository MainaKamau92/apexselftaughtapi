from apexselftaught.apps.authentication.models import User
from apexselftaught.apps.core.models import TimestampedModel, models


class Profile(TimestampedModel):
    first_name = models.CharField(max_length=250, null=True)
    middle_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    secondary_email = models.EmailField(max_length=250, null=True)
    user_bio = models.TextField(null=True)
    avatar = models.URLField(null=True)
    county = models.CharField(max_length=150, null=True)
    industry = models.CharField(max_length=255, null=True)
    github = models.URLField(null=True)
    linkendin = models.URLField(null=True)
    resume = models.URLField(null=True)
    website = models.URLField(null=True)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
