from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LoginForm


# Create your views here.
def register(request):
    return render(request, "register.html")


def update_profile(request):
    return render(request, "update_profile.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
    return render(request, "signin.html")


def user_logout(request):
    logout(request)
    return redirect("login")
