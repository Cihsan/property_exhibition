from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Account


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = email.split("@")[0]
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]
        user = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        user.save()
        return redirect("login")
    return render(request, "register.html")


def update_profile(request):
    return render(request, "update_profile.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("login success")
            return redirect("profile")
        else:
            redirect("login")
    return render(request, "signin.html")


def user_logout(request):
    logout(request)
    return redirect("login")
