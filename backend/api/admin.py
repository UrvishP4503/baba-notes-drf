from django.contrib import admin

from .models import Notes, User


class NotesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "category",
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "password",
        "userIdentificationNumber",
    ]


admin.site.register(Notes, NotesAdmin)
admin.site.register(User)
