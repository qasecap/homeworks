from django.contrib import admin
from django.urls import path

from posts.views import about, get_posts, hello, main

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("", main, name="home"),
    path("about/", about),
    path("posts/", get_posts, name="post_list"),
]
