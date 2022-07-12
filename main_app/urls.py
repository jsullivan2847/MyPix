from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/create', views.AddProfileForm, name = 'profile_form'),
    path('profile/new', views.AddProfile, name = 'profile_new'),
    path('profile/<int:profile_id>', views.ProfileShow, name='profile_show'),
    path('profile/<int:profile_id>/add_photo', views.AddProfilePhoto, name = 'profile_photo'),
    path('profile/<int:pk>/edit', views.EditProfile.as_view(), name='profile_update'),
    # PHOTOS
    path('profile/<int:profile_id>/post_photo', views.PostPhoto, name='post_photo'),
   
]