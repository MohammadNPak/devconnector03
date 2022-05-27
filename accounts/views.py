from django.shortcuts import render
from django.http import HttpResponse


def login_page(request):
    return render(request,'accounts/login.html',{})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def profile(request):
    return render(request,'accounts/profile.html',{})


def register(request):
    condext = {}
    return render(request,'accounts/register.html',condext)

def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

  
def create_profile(request):
    return render(request,'accounts/create-profile.html',{})

def add_education(request):
    return render(request,'accounts/add-education.html',{})

def add_experience(request):
    return render(request,'accounts/add-experience.html',{})
    


