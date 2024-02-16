from django.http import Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .authentication import Baba
from .models import Notes, User, Category
from .serializers import (
    NotesSerializer,
    UserSerializer,
    AuthTokenSerializer,
    CategorySerializer,
)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class NotesModelViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]

    authentication_classes = [
        Baba,
        TokenAuthentication,
    ]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    pagination_class = CustomPagination
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        user = request.user
        category = get_object_or_404(
            Category,
            name=request.data.get("category"),
            userIdentificationNumber=user.userIdentificationNumber,
        )

        data = {
            "title": request.data.get("title"),
            "content": request.data.get("content"),
            "category": category.id,
            "userIdentificationNumber": user.userIdentificationNumber,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.title = request.data.get("title", instance.title)
        instance.content = request.data.get("content", instance.content)
        if request.data.get("category"):
            category = get_object_or_404(
                Category,
                name=request.data.get("category"),
                userIdentificationNumber=request.user.userIdentificationNumber,
            )
            instance.category = category
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryModelViewSet(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        Baba,
        TokenAuthentication,
    ]
    serializer_class = CategorySerializer

    def post(self, request):
        user = request.user
        data = {
            "userIdentificationNumber": user.userIdentificationNumber,
            "name": request.data.get("name"),
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def delete(self, request, pk=None):
        if not pk:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "No id provided"},
            )
        category = get_object_or_404(Category, pk=pk)

        print(request.user.userIdentificationNumber)
        print(category.userIdentificationNumber)

        if request.user == category.userIdentificationNumber:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_403_FORBIDDEN)


class UserViewSet(CreateAPIView):
    serializer_class = UserSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        Baba,
        TokenAuthentication,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.user.userIdentificationNumber)
        return self.request.user


class DeleteUserView(DestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        Baba,
        TokenAuthentication,
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
    authentication_classes = [
        Baba,
        TokenAuthentication,
    ]

    def post(self, request):
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(settings.AUTH_COOKIE)

        return response
