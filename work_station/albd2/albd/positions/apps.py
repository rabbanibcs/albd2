from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PositionsConfig(AppConfig):
    name = 'albd.positions'
    verbose_name = _("Article Position")
