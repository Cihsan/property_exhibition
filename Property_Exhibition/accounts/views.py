from django.shortcuts import render,redirect 
from django.contrib.auth import logout

# Create your views here.
def register(request):
    return render(request, "register.html")

def update_profile(request):
    return render(request, "update_profile.html")

def user_login(request):
    return render(request, "signin.html")

def user_logout(request):
    logout(request)
    return redirect('login') 