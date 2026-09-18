from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "execution_date",
        "created_at",
    )
    list_filter = (
        "execution_date",
        "created_at",
    )
    search_fields = (
        "title",
        "content",
        "user__username",
    )
