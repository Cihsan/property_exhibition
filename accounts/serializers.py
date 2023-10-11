from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        read_only_fields = ("username", "email")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    current_address = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.gender = validated_data.get("gender", instance.gender)
        instance.contact_no = validated_data.get("contact_no", instance.contact_no)
        instance.area = validated_data.get("area", instance.area)
        instance.city = validated_data.get("city", instance.city)
        instance.district = validated_data.get("district", instance.district)
        instance.division = validated_data.get("division", instance.division)
        instance.parmanent_address = validated_data.get(
            "parmanent_address", instance.parmanent_address
        )
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.profile_avatar = validated_data.get(
            "profile_avatar", instance.profile_avatar
        )

        user_data = validated_data.get("user", {})
        user = instance.user

        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.save()

        instance.save()
        return instance
