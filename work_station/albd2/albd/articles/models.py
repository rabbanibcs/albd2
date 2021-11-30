# -*- coding: utf-8 -*-
import os
import re

from dateutil.relativedelta import relativedelta

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.translation import get_language

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from tinymce.models import HTMLField
from model_utils import Choices

from albd.categories.models import Category
from albd.content_types.models import ContentType
from albd.positions.models import Position
from django_comments.models import Comment


class ArticleManager(CurrentSiteManager):

    def published(self, limit=None, exclude_category='mujib-100'):
        lang = get_language()
        qs = self.get_queryset().filter(lang=lang).filter(publish_date__isnull=False). \
            filter(publish_date__lte=timezone.now())

        if exclude_category:
            qs = qs.exclude(category__slug=exclude_category)

        qs = qs.order_by('-publish_date')
        if limit:
            return qs[:limit]
        return qs

    def get_top_news(self, limit=5):
        return self.published().filter(position__rank__gte=0). \
                   order_by('position__rank')[:limit]

    def get_article_items(self, category_name=None, limit=5):

        if not category_name:
            return self.published()[:limit]

        return self.published().filter(category__slug=category_name)[:limit]

    def get_articles_in_focus(self, limit=10):
        return self.published().filter(in_focus=True).order_by('in_focus_order')[:limit]

    def get_gallery_items(self, content_type='photo', limit=None):
        qs = self.published().filter(category__slug='gallery', content_type__slug=content_type)
        if limit:
            return qs[:limit]
        return qs


def is_unicode(title):
    uc_pattern = re.compile("[^\x00-\x7F]")

    if uc_pattern.search(title):
        return True

    return False


def hexify_title(title):
    return "".join(["%04x" % ord(ch) for ch in title])


def unique_slug_generator(value):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    return default_slugify(value.title)


class Article(models.Model):
    SUB_CATEGORY = Choices('liberator', 'celebration', 'history', 'video', 'opinion')

    objects = models.Manager()
    on_site = ArticleManager()

    title = models.CharField(max_length=500, blank=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, editable=False, default=settings.SITE_ID)
    slug = AutoSlugField(populate_from=unique_slug_generator, max_length=1000)
    short_title = models.CharField(max_length=500, blank=True)
    snippet = models.TextField(blank=True)
    body = HTMLField()
    tags = TaggableManager()

    core_issue = models.CharField(max_length=1000, blank=True)
    seo_url = models.CharField(max_length=200, blank=True)
    meta_key = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=1000, blank=True)
    lang = models.CharField(max_length=10, choices=settings.LANGUAGES)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    sub_category = models.CharField(null=True, blank=True, max_length=20, choices=SUB_CATEGORY)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, editable=True)
    publish_date = models.DateTimeField(editable=True)

    author = models.CharField(blank=True, max_length=200, default=None)
    allow_comments = models.BooleanField(default=True, blank=False, editable=True)
    in_focus = models.BooleanField(verbose_name="Show in Focus", default=False)
    in_focus_order = models.IntegerField(verbose_name="Order in Focus", default=0, blank=True)

    courtesy = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def photos(self):
        return self.photo_list.order_by('order')

    def videos(self):
        return self.video_list.order_by('order')

    def attachments(self):
        return self.attachment_list.order_by('order')

    @property
    def video_url(self):
        url = ''
        video = self.video_list.first()
        if video:
            url = video.video_url

        return url

    @property
    def tag_list(self):
        return [o.name for o in self.tags.all()]

    @property
    def is_published(self):
        return self.publish_date is not None

    @property
    def icon_class(self):

        if self.content_type.slug == 'video':
            cls = 'fa-play-circle'
        elif self.content_type.slug == 'photo':
            cls = 'fa-camera'
        elif self.content_type.slug == 'download':
            cls = 'fa-download'
        else:
            cls = 'fa-newspaper-o'

        return cls

    @property
    def time_span(self):
        td = relativedelta(timezone.now(), self.publish_date)
        if td.years > 0:
            return "{} years".format(td.years)
        elif td.years == 0 and td.months > 0:
            return "{} months".format(td.months)
        elif td.years == 0 and td.months == 0 and td.days > 0:
            return "{} days".format(td.days)
        elif td.years == 0 and td.months == 0 and td.days == 0 and td.hours > 0:
            return "{} hours".format(td.hours)
        elif td.years == 0 and td.months == 0 and td.days == 0 and td.hours == 0 and td.minutes > 0:
            return "{} minutes".format(td.minutes)
        else:
            return "{} seconds".format(td.seconds)

    def approved_comments(self):
        return Comment.objects.for_model(self).filter(is_public=True)

    def unapproved_comments(self):
        return Comment.objects.for_model(self).filter(is_public=False)

    def total_comments(self):
        return Comment.objects.for_model(self)

    def __str__(self):
        return u"{}".format(self.title[:150])

    def get_absolute_url(self):
        content_type = "news"
        if self.category.slug in ['gallery', 'mujib-100']:
            content_type = self.content_type.slug

        return reverse('articles:detail', kwargs={
            'content_type': content_type,
            'article_id': self.id,
            'slug': "{}".format(self.title.replace(' ', '-'))})

    def get_previous(self):
        article = None
        try:
            # isnull is to check whether it's published or not - drafts don't have dates, apparently
            return Article.on_site.filter(publish_date__lt=self.date, publish_date__isnull=False)[0]
        except IndexError:
            # print 'Exception: %s' % e.message
            return None

    def get_next(self):
        try:
            # isnull is to check whether it's published or not - drafts don't have dates, apparently
            return Article.on_site.filter(publish_date__gt=self.date, publish_date__isnull=False).order_by('date')[0]
        except IndexError:
            # print 'Exception: %s' % e.message
            return None

    class Meta:
        ordering = ['-publish_date']
        unique_together = (('slug', 'publish_date', 'site'),)


class ArticlePhoto(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="photo_list")
    image = FilerImageField(on_delete=models.SET_NULL, null=True, blank=True)
    order = models.IntegerField(default=0)
    caption = models.CharField(blank=True, max_length=200)
    credit = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return u"{}".format(os.path.basename(self.image.file.name))


class ArticleVideo(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="video_list")
    video = FilerFileField(on_delete=models.SET_NULL, null=True, blank=True)
    order = models.IntegerField(default=0)
    fb_video = models.CharField(blank=True, max_length=250)
    youtube_url = models.CharField(blank=True, max_length=200)
    caption = models.CharField(blank=True, max_length=200)

    def __str__(self):
        if self.video:
            return u"{}".format(os.path.basename(self.video.file.name))

        return "Video # {}".format(self.pk)

    @property
    def video_url(self):
        url = self.youtube_url if self.youtube_url else self.video.file.url
        return url


class ArticleAttachment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="attachment_list")
    attachment = FilerFileField(on_delete=models.SET_NULL, null=True, blank=True)
    order = models.IntegerField(default=0)
    caption = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return u"{}".format(os.path.basename(self.attachment.file.name))
