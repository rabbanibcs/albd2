from django.contrib import admin

from .models import TopBanner

class TobBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'image', 'lang', 'is_published', 'show')
    list_filter = ('title', 'lang', 'type')


admin.site.register(TopBanner, TobBannerAdmin)




