from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.urls import reverse





class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('home')

class Photo(models.Model):
    photo_url = models.CharField(max_length=200)
    caption = models.CharField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

