from collections import OrderedDict

from django.template import Library

from albd.articles.models import Article

register = Library()


@register.simple_tag
def get_focus_news():
    menus = OrderedDict()

    for item in Article.on_site.get_articles_in_focus(limit=10):
        menus[item.get_absolute_url()] = item.title

    return menus
