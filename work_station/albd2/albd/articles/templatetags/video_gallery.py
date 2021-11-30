from collections import OrderedDict

from django.template import Library

from albd.articles.models import Article

register = Library()


@register.simple_tag
def get_video_gallery():
    menus = OrderedDict()

    for item in Article.on_site.published().filter(content_type__slug='video')[:5]:
        menus[item.get_absolute_url()] = item

    return menus
