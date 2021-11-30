from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PublicationsConfig(AppConfig):
    name = 'albd.publications'
    verbose_name = _("Publication")
