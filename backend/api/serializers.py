from rest_framework import serializers

from .models import Notes, User


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "userIdentificationNumber",
            "email",
            "username",
        ]
