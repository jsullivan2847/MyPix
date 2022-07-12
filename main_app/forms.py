from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic']