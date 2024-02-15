from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)


from .models import Notes, User, Category
from .serializers import (
    NotesSerializer,
    UserSerializer,
    AuthTokenSerializer,
    CategorySerializer,
)


class NotesModelViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Notes.objects.all().order_by("-updatedAt")[:25]

    def create(self, request, *args, **kwargs):
        user = request.user
        category = get_object_or_404(
            Category,
            name=request.data.get("category"),
            userIdentificationNumber=user.userIdentificationNumber,
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(userIdentificationNumber=user, category=category)

        return Response(status=status.HTTP_201_CREATED, data=serializer)


# TODO: add the category viewset


class UserViewSet(CreateAPIView):
    serializer_class = UserSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            token = response.data.get("token")

            response.set_cookie(
                settings.AUTH_COOKIE,
                token,
                max_age=settings.AUTH_COOKIE_AGE,
                path=settings.AUTH_COOKIE_PATH,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE,
            )

        return response


class LogoutView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(settings.AUTH_COOKIE)

        return response


class DeleteUserView(DestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_queryset(self):
        email = self.request.data.get("email")
        return User.objects.filter(email=email)

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset)

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
