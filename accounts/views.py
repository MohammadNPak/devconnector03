from django.shortcuts import render

# Create your views here.


def my_view(request):
    return render(request,'',{})

def register(request):
    condext = {}
    return render(request,'account\register.html',condext)