from rest_framework import serializers
from .models import Property, PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ("image",)


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, source="propertyimage_set")

    class Meta:
        model = Property
        fields = "__all__"

    def get_image_urls(self, obj):
        # Get image URLs for the property
        return [image.image.url for image in obj.images.all()]
