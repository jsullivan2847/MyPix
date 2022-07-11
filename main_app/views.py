from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Photo, User

def Home(request):
    if request.user.is_authenticated:
        user  = request.user
        profile = Profile.objects.get(id = user.id)
        return render(request,'home.html', {'profile': profile})
    else: return(render(request, 'home.html'))

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

class AddProfile(CreateView):
    model = Profile
    fields = '__all__'
    success_url = '/'

class ProfileShow(DetailView):
    model = Profile
    template_name = 'main_app/profile_show.html'

class EditProfile(UpdateView):
    model = Profile

class PhotoList(ListView):
    model = Photo

class AddPhoto(CreateView):
    model = Photo
    fields = '__all__'
    success_url = '/'