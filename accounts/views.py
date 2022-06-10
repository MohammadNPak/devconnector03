from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        # print(dir(request))
        if user:
            login(user)
            
        else:
            messages.add_message(request,messages.ERROR,"username or password is wrong!")
        # print(username,password)
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
    


