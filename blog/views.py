from django.shortcuts import render

# Create your views here.


def post(request):
    return render(request,'blog/post.html',{})

def index(request):
    return render(request,'blog/index.html',{})

def posts(request):
    return render(request,'blog/posts.html',{})
  

