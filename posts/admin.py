from django.contrib import admin

from posts.models import Author, Post, Tag

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
