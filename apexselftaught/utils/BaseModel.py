from django.db import models


class BaseModel(models.Model):
    """
    Common model variables are put here and inherited by all existing models
    """

    class Meta:
        abstract = True

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
