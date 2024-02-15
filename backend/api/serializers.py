from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from .models import Notes, User, Category


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "userIdentificationNumber",
            "name",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
                "required": True,
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user

        return attrs
