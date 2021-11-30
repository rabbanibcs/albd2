from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import get_language

from filer.fields.image import FilerImageField
from autoslug import AutoSlugField


class NewsletterManger(models.Manager):

    def get_published(self):
        lang = get_language()
        return self.get_queryset().filter(published__isnull=False). \
            filter(published__lte=timezone.now()).filter(lang__exact=lang)


class Newsletter(models.Model):
    lang = models.CharField(blank=False, max_length=10, choices=settings.LANGUAGES)
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title', ],
        max_length=100,
        allow_unicode=True,
        always_update=True,
        blank=True
    )
    thumbnail = FilerImageField(on_delete=models.CASCADE, null=True, blank=False)
    link = models.URLField(max_length=200, blank=False)
    published = models.DateTimeField(editable=True, auto_now_add=True)

    objects = NewsletterManger()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Newsletters"
        ordering = ['-published']
        unique_together = (('slug', 'published'),)

    @property
    def is_published(self):
        return self.published is not None
