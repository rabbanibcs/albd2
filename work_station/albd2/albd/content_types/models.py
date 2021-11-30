from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import get_language

# Create your models here.

class ContentType(models.Model):
    name = models.CharField(max_length=100, blank=False)
    bn_name = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name',],
        max_length=100,
        allow_unicode=True,
        always_update=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Content Types"

    def __str__(self):
        return self.name

    @property
    def label(self):
        lang = get_language()
        return self.bn_name if lang=='bn' else self.name

