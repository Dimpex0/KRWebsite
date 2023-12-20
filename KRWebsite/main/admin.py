from django.contrib import admin
from .models import Album, Image, Worker


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cover_image']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'image']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
