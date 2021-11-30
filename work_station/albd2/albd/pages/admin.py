from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'is_published')


admin.site.register(Page, PageAdmin)
