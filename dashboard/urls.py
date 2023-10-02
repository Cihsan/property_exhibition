from django.urls import path
from .views import (
    dashbaord_view,
    user_profile,
    all_property_manage,
    edit_profile,
    add_testimonial,
    promotions,
    all_promotions,
)

urlpatterns = [
    path("", dashbaord_view, name="dashboard"),
    path("user", user_profile, name="user_profile"),
    path("edit-profile", edit_profile, name="edit_profile"),
    path("properties", all_property_manage, name="all_properties"),
    path("testimonial", add_testimonial, name="testimonial"),
    path("add-promotions", promotions, name="add_promotions"),
    path("promotions", all_promotions, name="promotions"),
]
