from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.propertylist, name="property"),
    path("detail_property", views.detailproperty, name="detail_property"),
]
