from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/new', views.AddProfile.as_view(), name = 'profile_new'),
    path('profile/<int:pk>', views.ProfileShow.as_view(), name='profile_show'),
    path('profile/<int:pk>/edit', views.EditProfile.as_view(), name='profile_update'),
   
]