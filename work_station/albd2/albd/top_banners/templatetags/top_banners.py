from django.template import Library
from albd.top_banners.models import TopBanner

register = Library()


@register.simple_tag
def get_main_banners():
    return TopBanner.objects.get_published().filter(type__exact='M').all()


@register.simple_tag
def get_static_banners():
    return TopBanner.objects.get_published().filter(type__exact='S').all()
