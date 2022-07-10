from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('timeline/', views.TimeLine, name='timeline'),
]