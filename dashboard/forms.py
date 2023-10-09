from django import forms
from django.forms import ModelForm
from .models import Testimonial, Promotion
from django.forms import modelformset_factory
from all_property.models import Property, PropertyImage


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


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super(PropertyImageForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].label = "Image"


PropertyImageFormSet = forms.inlineformset_factory(
    Property,
    PropertyImage,
    form=PropertyImageForm,
    extra=4,
    can_delete=True,
)

EditPropertyImageFormSet = forms.inlineformset_factory(
    Property,
    PropertyImage,
    form=PropertyImageForm,
    extra=1,
    can_delete=True,
)
