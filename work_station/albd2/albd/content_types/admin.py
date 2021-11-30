from django.contrib import admin

# Register your models here.

from .models import ContentType

class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('name','slug','bn_name')

admin.site.register(ContentType, ContentTypeAdmin)
