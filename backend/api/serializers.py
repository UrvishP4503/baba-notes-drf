from rest_framework import serializers

from .models import Notes, User


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = [
            "title",
            "content",
            "category",
        ]


class NotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]

        extra_kwargs = {
            "email": {"required": True},
        }
