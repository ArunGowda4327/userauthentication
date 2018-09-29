from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    #why im using user onetoonefield means it has attribute username password email inside
    user = models.OneToOneField(User) #onetoone because it extends another 2 also pic and site

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.user.username
