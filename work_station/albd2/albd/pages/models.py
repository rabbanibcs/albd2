from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.urls import reverse
from django.utils import timezone

from tinymce import models as tinymce_models
from autoslug import AutoSlugField


class PageManager(CurrentSiteManager):

    def published(self, limit=None):
        qs = self.get_queryset().filter(published_date__isnull=False). \
            filter(published__lte=timezone.now()).order_by('-published_date')
        if limit:
            return qs[:limit]
        return qs


class Page(models.Model):
    objects = models.Manager()
    on_site = PageManager()

    title = models.CharField(max_length=100, blank=False)
    menu_label = models.CharField(max_length=100, blank=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    slug = models.CharField(max_length=100, unique=True)
    body = tinymce_models.HTMLField()

    published_date = models.DateTimeField(editable=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    lang = models.CharField(blank=False, max_length=10, choices=settings.LANGUAGES)

    class Meta:
        verbose_name_plural = "Pages"
        ordering = ['-published_date']
        unique_together = (('slug', 'published_date', 'site'),)

    def __str__(self):
        return self.title

    @property
    def is_published(self):
        return self.published_date is not None

    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={
            'slug': "{}".format(self.slug)})
