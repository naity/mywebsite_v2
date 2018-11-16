from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    # show the title, likes, and upload time for each photo
    list_display = ["title", "likes"]

    # allow search gene by title
    search_fields = ["tittle"]

    # show at most 10 photots per page
    list_per_page = 10


admin.site.register(Photo, PhotoAdmin)

