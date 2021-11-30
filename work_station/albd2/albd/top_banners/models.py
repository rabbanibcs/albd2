from django.conf import settings
from django.utils import timezone
from django.db import models
from django.utils.translation import get_language

from filer.fields.image import FilerImageField
from autoslug import AutoSlugField
from djchoices import DjangoChoices, ChoiceItem


class TopBannerManager(models.Manager):

    def get_published(self, limit=None):
        lang = get_language()
        return self.get_queryset().filter(published__isnull=False) \
            .filter(published__lte=timezone.now()).filter(show__exact=True) \
            .filter(lang__exact=lang)


class TopBanner(models.Model):
    class BannerType(DjangoChoices):
        Static = ChoiceItem('S')
        Main = ChoiceItem('M')

    lang = models.CharField(blank=False, max_length=10, choices=settings.LANGUAGES)
    title = models.CharField(max_length=255, blank=False)
    instruction = models.CharField(max_length=512, blank=True, null=True)
    type = models.CharField(max_length=2, blank=False, default='M', choices=BannerType.choices)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title', ],
        max_length=100,
        allow_unicode=True,
        always_update=True,
        blank=True
    )
    image = FilerImageField(on_delete=models.CASCADE, null=True, blank=False)
    link = models.URLField(max_length=200, blank=False)
    published = models.DateTimeField(editable=True, blank=True, null=True)
    show = models.BooleanField(default=False)
    show_instruction = models.BooleanField(default=True)
    objects = TopBannerManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Top Banners"
        ordering = ['-published']
        unique_together = (('slug', 'published'),)

    @property
    def is_published(self):
        return self.published is not None
