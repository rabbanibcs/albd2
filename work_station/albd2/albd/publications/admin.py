from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Publication

class PublicationAdmin(ImportExportModelAdmin):
    list_display = ['title', 'published', 'order', 'carousel_caption']

admin.site.register(Publication, PublicationAdmin)
