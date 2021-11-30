from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MessagingConfig(AppConfig):
    name = 'albd.messaging'
    verbose_name = _("Messaging")
