from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TopBannersConfig(AppConfig):
    name = 'albd.top_banners'
    verbose_name = _("Top Banner")
