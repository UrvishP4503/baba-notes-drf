from rest_framework.viewsets import ModelViewSet

from .models import Notes, User
from .serializers import NotesSerializer, UserSerializer


class NotesModelViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Notes.objects.all()[:25]


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = "email"

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)
