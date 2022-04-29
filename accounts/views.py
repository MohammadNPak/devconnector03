from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def register(request):
    condext = {}
    return render(request,'accounts/register.html',condext)

def dashboard(request):
    return render(request,'accounts/dashboard.html',{})

  
def create_profile(request):
    return render(request,'accounts/create-profile.html',{})
