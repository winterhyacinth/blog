from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "home.html", context)

def detail(request, pk):
    #get one specific post
    this_post = Post.objects.get(pk=pk)
    context = {
        "post": this_post
    }
    return render(request, "detail.html", context)