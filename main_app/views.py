from typing import List
from django.shortcuts import render
from django.views.generic import ListView

def Home(request):
    return render(request,'home.html')
    
