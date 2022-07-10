from multiprocessing import context
from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *

def Home(request):
    return render(request,'home.html')

def signup(request):
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
        else:
            error = "Invalid sign up, try again"
    form = UserCreationForm()
    context = {'form': form, 'error': error}
    return render(request, 'registration/signup.html', context)


# def TimeLine(request):
#     return render(request, 'home.html')

class PhotoList(ListView):
    model = Photo

class AddPhoto(CreateView):
    model = Photo
