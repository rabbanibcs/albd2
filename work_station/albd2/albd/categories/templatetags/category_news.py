from collections import OrderedDict

from django.utils.translation import get_language
from django.template import Library
from albd.categories.models import Category
from albd.articles.models import Article

register = Library()


@register.simple_tag
def get_category_news():
    menus = OrderedDict()
    lang = get_language()

    for item in Category.on_site.all():
        if Article.on_site.published(exclude_category=None).filter(category__slug=item.slug).exists():
            menus[item.get_url()] = item.bn_name if lang == 'bn' else item.name
    return menus
