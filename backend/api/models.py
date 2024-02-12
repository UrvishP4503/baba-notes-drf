from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notes"


# TODO: create user model
# TODO: figure out how to manage categories
# TODO: how the hell do I manage categories??
