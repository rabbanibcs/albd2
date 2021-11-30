from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Newsletter


@admin.register(Newsletter)
class NewletterAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'thumbnail', 'lang', 'is_published')
    list_filter = ('title', 'lang')
