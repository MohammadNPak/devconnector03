from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, SamplePost
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


# Create your views here.


def post(request, id):
    # p=Post.objects.filter(id=id).first()
    # try:
    #     p=Post.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     raise Http404("Poll does not exist")
    p = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment_body = request.POST.get("comment_body")
        if comment_body:
            c = Comment(body=comment_body,post=p)
            c.save()
    c = Comment.objects.filter(post=p).order_by('-date')
    return render(request, 'blog/post.html',
                    {'post': p, 'username': 'mohammadnpak', 'comments': c})

def index(request):
    return render(request, 'blog/index.html', {})


def posts(request):
    if request.method=="POST":
        title=request.POST.get("title")
        body=request.POST.get("body")
        if title and body:
            p = Post(title=title,body=body)
            p.save()
    posts = Post.objects.all().order_by('-date')[:20]

    return render(request, 'blog/posts.html', {"posts":posts})


def sample_post(request):
    if request.method == "GET":
        return render(request,
                      'blog/sample_post.html',
                      {"type": request.method})
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        sp = SamplePost(title=title, body=body)
        sp.save()

        return render(request,
                      'blog/sample_post.html',
                      {"message": "your data has been saved!"})
