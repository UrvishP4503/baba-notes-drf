from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Notes
from .serializers import NotesSerializer, NotesListSerializer, UserSerializer


class NotesViewSet(ViewSet):
    """
    ViewSet for managing notes.
    """

    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all notes.

        Returns:
            Response: HTTP response with a list of notes.
        """
        notes = Notes.objects.all().order_by("-updatedAt")
        notes_data = NotesListSerializer(notes, many=True).data

        return Response(status=status.HTTP_200_OK, data={"notes": notes_data})

    def create(self, request, *args, **kwargs):
        """
        Create a new note.

        Args:
            request (Request): HTTP request object containing the note data.

        Returns:
            Response: HTTP response with the created note.
        """
        note = NotesSerializer(data=request.data)

        note.is_valid(raise_exception=True)
        note.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": "Note created successfully", "note": note.data},
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific note.

        Args:
            request (Request): HTTP request object.

        Returns:
            Response: HTTP response with the retrieved note.
        """
        pass

    def update(self, request, *args, **kwargs):
        """
        Update a specific note.

        Args:
            request (Request): HTTP request object.

        Returns:
            Response: HTTP response indicating the success of the update.
        """
        pass

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a specific note.

        Args:
            request (Request): HTTP request object.

        Returns:
            Response: HTTP response indicating the success of the partial update.
        """
        pass
