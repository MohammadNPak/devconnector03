from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

  
def create_profile(request):
    return render(request,'accounts/create-profile.html',{})

