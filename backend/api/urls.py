from rest_framework.routers import DefaultRouter

from .views import NotesViewSet

routers = DefaultRouter()

routers.register(r"notes", NotesViewSet, basename="notes")


urlpatterns = routers.urls
