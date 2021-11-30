from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils import timezone
from django.utils.translation import get_language

from filer.fields.image import FilerImageField
from autoslug import AutoSlugField


class PublicationManager(CurrentSiteManager):

    def published(self, limit=None):
        lang = get_language()

        qs = self.get_queryset().filter(published__isnull=False). \
            filter(published__lte=timezone.now()).filter(lang=lang) \
            .order_by('published', 'order')

        if limit:
            return qs[:limit]
        return qs


class Publication(models.Model):
    objects = PublicationManager()

    title = models.CharField(blank=True, max_length=200)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title', ],
        max_length=100,
        allow_unicode=True,
        always_update=True,
        blank=True
    )
    lang = models.CharField(blank=False, max_length=10, choices=settings.LANGUAGES)
    cover_page = FilerImageField(on_delete=models.CASCADE, null=True, blank=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    carousel_caption = models.CharField(blank=True, max_length=250)
    url = models.URLField(null=True)
    order = models.IntegerField(default=0, blank=True)
    published = models.DateTimeField(editable=True, auto_now_add=True)
    short_description = models.CharField(blank=True, max_length=500, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Publications"
        ordering = ['-published']
        unique_together = (('slug', 'published', 'site'),)

    @property
    def is_published(self):
        return self.published is not None
