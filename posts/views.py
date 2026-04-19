from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from posts.models import Post, Tag


def hello(request):
    return HttpResponse("Hello Django!")


def main(request):
    return render(request, "base.html")


def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")


def get_posts(request):
    tag_id = request.GET.get("tag")
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    if tag_id:
        posts = posts.filter(tags__id=tag_id)
    tags = Tag.objects.all()
    return render(request, "posts/posts_view.html", context={"posts": posts, "tags": tags, "selected_tag": tag_id})


def get_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/post_detail.html", context={"post": post})
