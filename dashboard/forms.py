from django.forms import ModelForm
from accounts.models import Account
from .models import Testimonial


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
