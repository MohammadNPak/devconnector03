from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your views here.


def post(request,id):
    # p=Post.objects.filter(id=id).first()
    # try:
    #     p=Post.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     raise Http404("Poll does not exist")
    p=get_object_or_404(Post,id=id)
    
    c=Comment.objects.filter(post=p)
    return render(request,'blog/post.html',
    {'post':p,'username':'mohammadnpak','comments':c})

def index(request):
    return render(request,'blog/index.html',{})

def posts(request):
    return render(request,'blog/posts.html',{})
  

