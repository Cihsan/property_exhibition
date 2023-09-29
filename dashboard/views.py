from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from accounts.models import Account


# Create your views here.
@login_required
def dashbaord_view(request):
    return render(request, "dashboard.html")


@login_required
def user_profile(request):
    return render(request, "user_profile.html")


@login_required
def edit_profile(request):
    user = Account.objects.get(email=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
    else:
        form = EditProfileForm(instance=user)

    return render(request, "edit_profile.html", {"form": form})


@login_required
def all_property_manage(request):
    return render(request, "all_properties.html")
