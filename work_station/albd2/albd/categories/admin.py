from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'bn_name']


admin.site.register(Category, CategoryAdmin)
