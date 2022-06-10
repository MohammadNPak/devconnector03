from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages

from accounts.models import User

def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        # print(dir(request))
        if user:
            login(request,user)
            return redirect(to=reverse('dashboard'))
        else:
            messages.add_message(request,messages.ERROR,"username or password is wrong!")
        # print(username,password)
    return render(request,'accounts/login.html',{})

def logout_page(request):
    logout(request)
    return redirect(to=reverse('index'))

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def profile(request,id):
    user=User.objects.get(id=id)
    return render(request,'accounts/profile.html',{"user":user})


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
    


