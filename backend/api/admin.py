from django.contrib import admin

from .models import Notes


class NotesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "category",
    ]


admin.site.register(Notes, NotesAdmin)
