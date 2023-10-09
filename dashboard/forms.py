from django import forms
from django.forms import ModelForm
from .models import Testimonial, Promotion
from django.forms import modelformset_factory
from all_property.models import Property


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


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
