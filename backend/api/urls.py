from django.urls import path
from .views import get_notes, create_note

urlpatterns = [
    path("notes", get_notes, name="get_notes"),
    path("create-note", create_note, name="create_note"),
]
