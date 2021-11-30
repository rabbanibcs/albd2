from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _, get_language

from djchoices import DjangoChoices, ChoiceItem
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class ItemManager(models.Manager):
    def in_order(self):
        return self.get_queryset().filter(status=GalleryItem.STATUS.published).order_by('order')


class GalleryManager(models.Manager):

    def published(self):
        lang = get_language()
        return self.get_queryset().filter(lang=lang, show=True)


class Gallery(models.Model):
    class GalleryType(DjangoChoices):
        video = ChoiceItem('video', 'General Video')
        info = ChoiceItem('info', 'InfoGraphic')
        history = ChoiceItem('history', 'History')
        live = ChoiceItem('live', 'Live')

    lang = models.CharField(blank=False, max_length=5, choices=settings.LANGUAGES)
    name = models.CharField(blank=False, max_length=200)
    type = models.CharField(blank=False, max_length=20, choices=GalleryType.choices)
    order = models.IntegerField(blank=True, default=0)
    publish_date = models.DateTimeField(editable=True)
    show = models.BooleanField(default=True)
    objects = GalleryManager()

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return "{}-{}".format(self.name, self.lang)

    @property
    def is_published(self):
        return self.publish_date is not None and self.publish_date < timezone.now()

    @property
    def no_of_items(self):
        return self.items.count()


class GalleryItem(models.Model):

    class SourceType(DjangoChoices):
        Youtube = ChoiceItem('youtube')
        Vimeo = ChoiceItem('vimeo')
        Local = ChoiceItem('local')
        Facebook = ChoiceItem('facebook')

    STATUS = Choices((0, 'draft', _('Draft')), (1, 'published', _('Published')))
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(blank=False, max_length=200)
    caption = models.CharField(blank=False, max_length=255)
    source = models.CharField(blank=False, max_length=10, choices=SourceType.choices)
    embedded_link = models.URLField("Embedded Link", blank=True, max_length=200)
    image = FilerImageField(on_delete=models.CASCADE, null=True, blank=True, related_name='thumbnail')
    video = FilerFileField(on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=STATUS.published)

    objects = ItemManager()

    class Meta:
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return self.title

    @property
    def get_item_link(self):
        if self.source in ('youtube', 'vimeo', 'facebook'):
            return self.embedded_link
        else:
            return self.video.file.url
