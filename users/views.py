from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from users.forms import EditProfileForm, LoginForm, RegisterForm


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data.get("username"))
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            return redirect("home")
        return render(request, "users/register.html", {"form": form})


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("home")
            form.add_error(None, "Введённый логин или пароль неверные!")
        return render(request, "users/login.html", {"form": form})


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user:
            logout(request)
        return redirect("home")


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = EditProfileForm(initial={"username": request.user.username})
        return render(request, "users/edit_profile.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = EditProfileForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data["username"]
            request.user.save()
            return redirect("home")
        return render(request, "users/edit_profile.html", {"form": form})
