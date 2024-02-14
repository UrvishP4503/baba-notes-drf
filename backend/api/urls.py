from rest_framework.routers import DefaultRouter

from .views import NotesModelViewSet, UserModelViewSet

routers = DefaultRouter()

routers.register(r"notes", NotesModelViewSet, basename="notes")
routers.register(r"user", UserModelViewSet, basename="user")


urlpatterns = routers.urls
