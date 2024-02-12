from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Notes
from .serializers import NotesSerializer, NotesListSerializer


@api_view(["GET"])
def get_notes(request, *args, **kwargs):
    notes = Notes.objects.all()
    notes_data = NotesListSerializer(notes, many=True).data

    return Response(status=200, data={"notes": notes_data})


@api_view(["POST"])
def create_note(request, *args, **kwargs):
    instance = NotesSerializer(data=request.data)

    if instance.is_valid():
        instance.save()
        return Response(
            status=200,
            data={"message": "Note created successfully", "note": instance.data},
        )

    return Response(status=400, data={"message": "Note creation failed"})
