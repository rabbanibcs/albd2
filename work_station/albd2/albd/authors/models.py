from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

from albd.users.models import User


class Author(models.Model):
    objects = models.Manager()
    on_site = CurrentSiteManager()

    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique_with=['name', 'site'], sep='-')

    def __str__(self):
        return self.name
