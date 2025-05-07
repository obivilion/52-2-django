from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post

def index(requset):
    return HttpResponse(f"Hello world, {randint(0, 100)}")

def homepage_view(request):
    return render(request, "base.html")

def html_view(requset):
    return render(requset, "test.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", context={"posts": posts})

# Create your views here.
