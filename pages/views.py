from django.shortcuts import render
from .models import Post

# Create your views here.

def home (request):
    #collects all posts we've written
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "home.html", context)
