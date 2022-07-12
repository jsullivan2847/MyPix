from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Profile, Photo

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name']

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['caption']