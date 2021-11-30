import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from albd.utils.utils import StringUtils
from albd.joinus.models import JoinUs
from albd.messaging.models import Message


class Command(BaseCommand):

    help = "Sending Message commands"
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('msg_id', nargs='?', type=int)
        parser.add_argument('target_options', nargs='?', type=str)

    def handle(self, *args, **options):

        msg_urls = []
        msg_instance = Message.objects.get(id=options.get('msg_id'))
        targets = options.get('target_options')
        # district=1&division=1@constituency=1&gender=1

        # ToDo: Need to add filters from target options

        groups = []

        recipients = JoinUs.recipients.valid_recipients()
        total_recipients = recipients.count()

        for index in range(0, total_recipients, 20):
            subgroups = []

            for recipient in recipients[index:index+20]:
                mobile_number = recipient.mobile.replace("+", '').replace(" ", '').replace("-", '')
                if StringUtils.is_unicode(mobile_number):
                    mobile_number = StringUtils.convert_bangla_digit_to_english_digit(mobile_number)

                mobile_number = "880" + mobile_number[-10:len(mobile_number)]
                subgroups.append(mobile_number)


            sms_kwargs = {'username': settings.SMS_USER, 'api_key': settings.SMS_API_KEY,
                          'sender': settings.SMS_USER, 'receiver': ",".join(subgroups), 'message': msg_instance.text}

            sms_url = settings.SMS_API.format(**sms_kwargs)

            requests.get(sms_url)

