from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, SamplePost
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import PostForm, CommentForm

# Create your views here.


def post(request, id):

    p = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid:
            comment_object = comment.save(commit=False)
            comment_object.post = p
            comment_object.save()

    c = Comment.objects.filter(post=p).order_by('-date')
    form = CommentForm()
    return render(request, 'blog/post.html',
                  {'post': p,
                   'username': 'mohammadnpak',
                   'comments': c,
                   'form': form
                   })


def index(request):
    return render(request, 'blog/index.html', {})


def posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
    posts = Post.objects.all().order_by('-date')[:20]
    form = PostForm()
    return render(request,
                  'blog/posts.html',
                  {"posts": posts,
                   "form": form})


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
