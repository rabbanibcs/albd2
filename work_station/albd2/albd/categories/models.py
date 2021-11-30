from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.utils.translation import get_language
from django.urls import reverse

from autoslug import AutoSlugField


class Category(models.Model):
    objects = models.Manager()
    on_site = CurrentSiteManager()

    name = models.CharField(max_length=100, blank=False)
    bn_name = models.CharField(verbose_name="Name in Bangla", max_length=100, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name', ],
        max_length=100,
        allow_unicode=True,
        always_update=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_url(self):
        if self.slug == 'mujib-100':
            return reverse('mujib100:index')

        return reverse('categories:detail', kwargs={
            'slug': "{}".format(self.slug)})

    @property
    def label(self):
        lang = get_language()
        return self.bn_name if lang == 'bn' else self.name
