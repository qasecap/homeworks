from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def hello(request):
    return HttpResponse("Hello Django!")


def main(request):
    return render(request, "base.html")


def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")


def get_posts(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "posts/posts_view.html", context={"posts": posts})
