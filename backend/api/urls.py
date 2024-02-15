from django.urls import path
from .views import (
    NotesModelViewSet,
    UserViewSet,
    RetrieveUpdateUserView,
    CustomAuthToken,
    LogoutView,
    DeleteUserView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"notes", NotesModelViewSet, basename="notes")

urlpatterns = [
    path("users/create", UserViewSet.as_view(), name="create-user"),
    path("users/me/", RetrieveUpdateUserView.as_view(), name="retrieve-update-user"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/user/", DeleteUserView.as_view(), name="delete-user"),
]

urlpatterns += router.urls
