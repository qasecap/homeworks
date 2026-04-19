from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from posts.models import Post, Tag


def hello(request):
    return HttpResponse("Hello Django!")


def main(request):
    return render(request, "base.html")


def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")


class PostsListView(ListView):
    model = Post
    template_name = "posts/posts_view.html"
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        tag_id = self.request.GET.get("tag")
        posts = Post.objects.filter(is_published=True).order_by("-published_at")
        if tag_id:
            posts = posts.filter(tags__id=tag_id)
        return posts

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["selected_tag"] = self.request.GET.get("tag")
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
