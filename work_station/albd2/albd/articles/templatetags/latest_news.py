from collections import OrderedDict

from django.template import Library

from albd.articles.models import Article

register = Library()


@register.simple_tag
def get_latest_news():
    menus = OrderedDict()

    for item in Article.on_site.published().filter(category__slug='news')[:5]:
        menus[item.get_absolute_url()] = item

    return menus
