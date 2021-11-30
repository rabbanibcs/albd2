from collections import OrderedDict

from django.template import Library
from albd.pages.utils import get_category_page_titles

register = Library()


@register.simple_tag
def get_category_menu():

    menus = OrderedDict()

    for item in get_category_page_titles():
        menus[item.get_absolute_url()] = item.menu_label

    return menus
