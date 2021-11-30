from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentTypesConfig(AppConfig):
    name = 'albd.content_types'
    verbose_name = _("Content Type")
