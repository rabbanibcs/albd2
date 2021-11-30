from django.template import Library

from albd.articles.models import Article

register = Library()


@register.simple_tag
def get_opinion_updates():
    return Article.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                   sub_category=Article.SUB_CATEGORY.opinion)[:2]
