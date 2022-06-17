from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Post,Comment
from .forms import PostForm, CommentForm

# Create your views here.


@login_required(login_url='/accounts/login/')
def post(request, id):
    # u = get_user_model().objects.first()
    p = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid:
            comment_object = comment.save(commit=False)
            comment_object.post = p
            comment_object.author = request.user
            comment_object.save()

    c = Comment.objects.filter(post=p).order_by('-date')
    form = CommentForm()
    return render(request, 'blog/post.html',
                  {'post': p,
                   'comments': c,
                   'form': form
                   })


def index(request):
    return render(request, 'blog/index.html', {})


@login_required
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

