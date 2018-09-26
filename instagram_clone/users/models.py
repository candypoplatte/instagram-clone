from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    MALE, FEMALE, NOTSPECIFIED = 'male', 'female', 'not-specified'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NOTSPECIFIED, 'Not specified'),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    following = models.ManyToManyField('self')
    followers = models.ManyToManyField('self')

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
