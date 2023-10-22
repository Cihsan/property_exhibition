from rest_framework import serializers
from .models import Property, Property_Images


class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Images
        fields = ("url",)


class PropertySerializer(serializers.ModelSerializer):
    property_images = PropertyImagesSerializer(
        source="property_images_set", many=True, read_only=True
    )

    class Meta:
        model = Property
        fields = "__all__"


class PropertyImagesCreateSerializer(serializers.Serializer):
    property_id = serializers.IntegerField()
    urls = serializers.ListField(child=serializers.URLField())
