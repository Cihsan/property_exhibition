from decimal import Decimal
import random
import string
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from all_property.models import Property


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
from sslcommerz_lib import SSLCOMMERZ


# testimonial api view
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def create(self, request, *args, **kwargs):
        property_id = request.data.get("property")
        if Promotion.objects.filter(property=property_id).exists():
            return Response(
                {"error": "A promotion for this property already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super(PromotionViewSet, self).create(request, *args, **kwargs)


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourites.objects.all()
    serializer_class = FavouriteSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "This combination already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_queryset(self):
        return Favourites.objects.filter(user=self.request.user)


class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


Store_ID = "prope652e86dbd1b13"
Store_Password = "prope652e86dbd1b13@ssl"
SUCCESS_URL = "https://property-exhibition.onrender.com/success"
FAIL_URL = "http://localhost:5173/failed"
CANCEL_URL = "https://property-exhibition.onrender.com/cancel"


def unique_trangection_id_generator(
    size=10, chars=string.ascii_uppercase + string.digits
):
    return "".join(random.choice(chars) for _ in range(size))


def payment_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("user")
            property_id = data.get("property")
            user = User.objects.get(id=user_id)
            property = Property.objects.get(id=property_id)
            settings = {
                "store_id": Store_ID,
                "store_pass": Store_Password,
                "issandbox": True,
            }

            sslcommez = SSLCOMMERZ(settings)
            post_body = {}
            post_body["total_amount"] = (Decimal(property.price),)
            post_body["currency"] = "BDT"
            post_body["tran_id"] = unique_trangection_id_generator()
            post_body["success_url"] = SUCCESS_URL + "/" + post_body["tran_id"]
            post_body["fail_url"] = FAIL_URL + "/" + post_body["tran_id"]
            post_body["cancel_url"] = CANCEL_URL + "/" + post_body["tran_id"]
            post_body["emi_option"] = 0
            post_body["cus_email"] = user.email
            post_body["cus_phone"] = user.userprofile.contact_no or "0123456789"
            post_body["cus_add1"] = user.userprofile.current_address()
            post_body["cus_city"] = user.userprofile.city or "Not given"
            post_body["cus_country"] = "Bangladesh"
            post_body["shipping_method"] = "NO"
            post_body["multi_card_name"] = ""
            post_body["num_of_item"] = 1
            post_body["product_name"] = property.title
            post_body["product_category"] = property.type
            post_body["product_profile"] = "RealEstate"
            response = sslcommez.createSession(post_body)
            booking_order = Booking.objects.create(
                user=user,
                property=property,
                total_amount=int(property.price),
                trans_id=post_body["tran_id"],
                payment_status="Pending",
            )
            booking_order.save()
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)


def complete_transaction(request, tran_id):
    booking = Booking.objects.get(trans_id=tran_id)
    if booking is not None:
        booking.payment_status = "Completed"
        booking.save()
        return redirect("http://localhost:5173/")
    else:
        return JsonResponse("Something went wrong")


def cancel_transaction(request, tran_id):
    booking = Booking.objects.get(trans_id=tran_id)
    if booking is not None:
        booking.payment_status = "Canceled"
        booking.save()
        return redirect("http://localhost:5173/property/")
    else:
        return JsonResponse("Something went wrong")
