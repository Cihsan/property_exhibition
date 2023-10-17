from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from all_property.models import Property

from dashboard.forms import PromotionForm, PropertyForm, TestimonialForm

from .models import Testimonial, Promotion, Favourites, Booking

# api
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Testimonial
from .serializers import (
    TestimonialSerializer,
    PromotionSerializer,
    FavouriteSerializer,
    BookingSerializer,
)
from accounts.permissions import IsOwnerOnly


# Create your views here.
@login_required(login_url="login")
def dashbaord_view(request):
    return render(request, "dashboard.html")


@login_required(login_url="login")
def user_profile(request):
    return render(request, "user_profile.html")


@login_required(login_url="login")
def edit_profile(request):
    user = User.objects.get(email=request.user)

    if request.method == "POST":
        form = PromotionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
    else:
        form = PromotionForm(instance=user)

    return render(request, "edit_profile.html", {"form": form})


@login_required(login_url="login")
def all_property_manage(request):
    properties = Property.objects.all()
    return render(request, "all_properties.html", {"properties": properties})


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


@login_required(login_url="login")
def create_property(request):
    if request.method == "POST":
        property_form = PropertyForm(request.POST)
        if property_form.is_valid():
            property_form.save()
            return redirect("dashboard")
    else:
        property_form = PropertyForm()

    context = {
        "property_form": property_form,
    }

    return render(request, "add_property.html", context)


@login_required(login_url="login")
def edit_property(request, id):
    property_instance = get_object_or_404(Property, id=id)

    if request.method == "POST":
        property_form = PropertyForm(request.POST, instance=property_instance)

        if property_form.is_valid():
            property_form.save()

            return redirect("all_properties")
    else:
        property_form = PropertyForm(instance=property_instance)

    context = {
        "property_form": property_form,
    }

    return render(request, "edit_property.html", context)


# testimonial api view
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourites.objects.all()
    serializer_class = FavouriteSerializer


class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
