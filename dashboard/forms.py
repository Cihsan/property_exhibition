from django.forms import ModelForm
from accounts.models import Account


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
