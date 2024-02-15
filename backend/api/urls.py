from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    NotesModelViewSet,
    UserViewSet,
    RetrieveUpdateUserView,
    CustomAuthToken,
    LogoutView,
    DeleteUserView,
    CategoryModelViewSet,
)


router = DefaultRouter()
router.register(r"notes", NotesModelViewSet, basename="notes")

urlpatterns = [
    path("users/create", UserViewSet.as_view(), name="create-user"),
    path("users/me/", RetrieveUpdateUserView.as_view(), name="retrieve-update-user"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/user/", DeleteUserView.as_view(), name="delete-user"),
    path("category/", CategoryModelViewSet.as_view(), name="category-create"),
    path("category/<int:pk>", CategoryModelViewSet.as_view(), name="category-delete"),
]

urlpatterns += router.urls
