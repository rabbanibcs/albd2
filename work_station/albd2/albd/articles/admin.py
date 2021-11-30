from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Article, ArticlePhoto, ArticleVideo, ArticleAttachment
from .forms import ArticleForm, ArticlePhotoForm, ArticleAttachmentForm, ArticleVideoForm


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhoto
    extra = 3
    form = ArticlePhotoForm
    verbose_name = "Photo"
    verbose_name_plural = "Photos"
    suit_classes = 'suit-tab suit-tab-photos'


class ArticleVideoInline(admin.TabularInline):
    model = ArticleVideo
    extra = 3
    form = ArticleVideoForm
    verbose_name = "Video"
    verbose_name_plural = "Videos"
    suit_classes = 'suit-tab suit-tab-videos'


class ArticleAttatmentInline(admin.TabularInline):
    model = ArticleAttachment
    extra = 3
    form = ArticleAttachmentForm
    verbose_name = "Attachment"
    verbose_name_plural = "Attachments"
    suit_classes = 'suit-tab suit-tab-attachments'


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    inlines = [ArticlePhotoInline, ArticleVideoInline, ArticleAttatmentInline]
    form = ArticleForm
    list_display = ('title','publish_date', 'lang', 'category', 'sub_category', 'content_type', 'position', 'is_published')
    list_filter = ['lang', 'category', 'sub_category', 'content_type', 'position']
    search_fields = ['title', ]
    ordering = ['-publish_date']

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['lang', 'title', 'short_title', 'body', 'snippet', 'category', 'sub_category', 'content_type', 'publish_date',
                       'author', 'tags', 'position', 'in_focus', 'in_focus_order', 'allow_comments',]
        }),
        ('SEO', {
            'classes': ('suit-tab', 'suit-tab-seo',),
            'fields': ['meta_key', 'meta_description', 'seo_url', 'core_issue', 'courtesy',]}),
    ]

    suit_form_tabs = (('general', 'General'), ('seo', 'SEO'), ('photos', 'Photos'), ('videos', 'Videos'), ('attachments', 'Attachments'))

