from django.urls import path
from .views import dashbaord_view

urlpatterns = [
    path("", dashbaord_view, name="dashboard"),
]
