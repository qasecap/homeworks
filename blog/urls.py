from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import PostDetailView, PostsListView, about, hello, main
from users.views import EditProfileView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("", main, name="home"),
    path("about/", about),
    path("posts/", PostsListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("users/register/", RegisterView.as_view(), name="register"),
    path("users/login/", LoginView.as_view(), name="login"),
    path("users/logout/", LogoutView.as_view(), name="logout"),
    path("users/profile/edit/", EditProfileView.as_view(), name="edit_profile"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
