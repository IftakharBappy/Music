from django.contrib import admin
from .models import Album


class MusicAdmin(admin.ModelAdmin):
    search_fields = "artist",
    list_display = ("artist", "album_title", "genre")
    list_filter = ("artist", "album_title")


admin.site.register(Album, MusicAdmin)

