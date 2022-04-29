from django.shortcuts import render

# Create your views here.


def posts(request):
    return render(request,'blog/posts.html',{})