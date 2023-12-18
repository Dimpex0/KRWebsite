from django.contrib import admin
from .models import Album, Image


@admin.register(Album)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover_image']


@admin.register(Image)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['album', 'image']
