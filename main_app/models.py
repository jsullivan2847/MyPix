import profile
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


class Profile(models.Model):
    name = CharField(max_length=100)
    profile_pic = CharField(max_length=200)

class Photo(models.Model):
    photo_url = CharField(max_length=200)
    caption = CharField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


