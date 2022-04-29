from django.shortcuts import render

# Create your views here.


def login_page(request):
    return render(request,'accounts/login.html',{})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def profile(request):
    return render(request,'accounts/profile.html',{})