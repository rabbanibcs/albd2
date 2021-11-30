from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LiveTVConfig(AppConfig):
    name = 'albd.livetv'
    verbose_name = _("Live TV")
