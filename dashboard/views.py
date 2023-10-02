from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, TestimonialForm, PromotionForm
from accounts.models import Account
from .models import Testimonial, Promotion


# Create your views here.
@login_required(login_url="login")
def dashbaord_view(request):
    return render(request, "dashboard.html")


@login_required(login_url="login")
def user_profile(request):
    return render(request, "user_profile.html")


@login_required(login_url="login")
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


@login_required(login_url="login")
def all_property_manage(request):
    return render(request, "all_properties.html")


@login_required(login_url="login")
def add_testimonial(request):
    user = request.user
    testimonial = Testimonial.objects.filter(user=user).first()

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = user
            testimonial.save()
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, "testimonial.html", {"form": form})


@login_required(login_url="login")
def promotions(request):
    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect("promotions")
    form = PromotionForm()
    return render(request, "add_promotions.html", {"form": form})


def all_promotions(request):
    user = request.user
    datas = Promotion.objects.filter(user=user)
    return render(request, "all_promotions.html", {"datas": datas})
