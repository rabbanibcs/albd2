from django.template import Library
from albd.livetv.models import LiveTV

register = Library()


@register.simple_tag
def get_livetv_info():
    return LiveTV.objects.first()
