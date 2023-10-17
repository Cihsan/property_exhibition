from decimal import Decimal
from django.http import JsonResponse
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

# from pysslcmz.payment import SSLCSession


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


Store_ID = "prope652e86dbd1b13"
Store_Password = "prope652e86dbd1b13@ssl"
SUCCESS_URL = "http://localhost:5173/success"
FAIL_URL = "http://localhost:5173/failed"
CANCEL_URL = "http://localhost:5173/cancel"


# def payments_view(request):
#     if request.metod == "POST":
#         user_id = request.POST.get("user")
#         property_id = request.POST.get("property")
#         user = User.objects.get(id=user_id)
#         property = Property.objects.get(id=property_id)
#         mypayment = SSLCSession(
#             sslc_is_sandbox=True, sslc_store_id=Store_ID, sslc_store_pass=Store_Password
#         )
#         mypayment.set_urls(
#             success_url=SUCCESS_URL,
#             fail_url=FAIL_URL,
#             cancel_url=CANCEL_URL,
#             ipn_url="example.com/payment_notification",
#         )
#         mypayment.set_product_integration(
#             total_amount=Decimal(property.price),
#             currency="BDT",
#             product_category=property.type,
#             product_name=property.title,
#             num_of_item=1,
#             shipping_method="NO",
#             product_profile="None",
#         )
#         mypayment.set_customer_info(
#             name=user.first_name,
#             email=user.email,
#             address1=user.user_userprofile.current_address(),
#             address2=user.user_userprofile.area,
#             city=user.user_userprofile.city,
#             postcode="0000",
#             country="Bangladesh",
#             phone=user.user_userprofile.contact_no,
#         )

#         mypayment.set_shipping_info(
#             shipping_to="demo customer",
#             address="demo address",
#             city="Dhaka",
#             postcode="1209",
#             country="Bangladesh",
#         )
#         response_data = mypayment.init_payment()
#         return JsonResponse(response_data)
