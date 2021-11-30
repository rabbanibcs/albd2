from django.contrib import admin

from .models import Gallery, GalleryItem


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'lang', 'show', 'no_of_items')
    list_filter = ('type', 'lang', 'show')


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'title', 'status', 'embedded_link', 'image', 'video')
    list_filter = ('gallery',)
