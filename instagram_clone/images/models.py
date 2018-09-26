from django.db import models
from django.db.models import SET_NULL

from instagram_clone.users.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):
    """Image Model"""

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(User, null=True, on_delete=SET_NULL)


class Comment(TimeStampedModel):
    """Comment Model"""

    message = models.TextField()
    creator = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    image = models.ForeignKey(Image, null=True, on_delete=SET_NULL)


class Like(TimeStampedModel):
    """Like Model"""

    creator = models.ForeignKey(User, null=True, on_delete=SET_NULL)
