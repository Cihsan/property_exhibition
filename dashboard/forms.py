from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from accounts.models import Account
from .models import Testimonial, Promotion


class EditProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "profile_picture",
            "address",
            "city",
            "state",
            "country",
        ]


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"
        exclude = ["user"]


class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "start_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
