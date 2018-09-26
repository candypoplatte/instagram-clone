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

    def __str__(self):
        return f'{self.location} -{self.caption}'


class Comment(TimeStampedModel):
    """Comment Model"""

    message = models.TextField()
    creator = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    image = models.ForeignKey(Image, null=True, on_delete=SET_NULL, related_name='comments')

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    """Like Model"""

    creator = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    image = models.ForeignKey(Image, null=True, on_delete=SET_NULL, related_name='likes')

    def __str__(self):
        return f'User : {self.creator.username} - Image caption : {self.image.caption}'
