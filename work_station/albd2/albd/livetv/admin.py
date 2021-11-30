from django.contrib import admin

from .models import LiveTV


class LiveTVAdmin(admin.ModelAdmin):
    list_display = ('name', 'embedded_link')


admin.site.register(LiveTV, LiveTVAdmin)
