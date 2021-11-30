# -*- coding: utf-8 -*-
import requests
import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from tinymce.models import HTMLField

from albd.joinus.models import JoinUs, District, Division, Constituency
from albd.contacts.models import Contact, Designation
from albd.utils.utils import StringUtils


class Message(models.Model):
    mobile = models.CharField(_("Mobile"), blank=True, null=True, max_length=13)
    include_joinus = models.BooleanField(_("Include Joinus"), default=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, related_name='messages', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, related_name='messages', blank=True, null=True)
    constituency = models.ForeignKey(Constituency, on_delete=models.SET_NULL, related_name='messages', blank=True,
                                     null=True)

    include_contacts = models.BooleanField(_("Include Contacts"), default=False)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)

    subject = models.CharField(max_length=100, blank=False)
    text = models.CharField(max_length=960, blank=False)
    write_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Email(models.Model):
    email = models.CharField(_("Email"), blank=True, null=True, max_length=100)
    include_joinus = models.BooleanField(_("Include Joinus"), default=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, related_name='email', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, related_name='email', blank=True, null=True)
    constituency = models.ForeignKey(Constituency, on_delete=models.SET_NULL, related_name='email', blank=True,
                                     null=True)

    include_contacts = models.BooleanField(_("Include Contacts"), default=False)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)

    subject = models.CharField(max_length=100, blank=False)
    text = HTMLField(blank=False)
    write_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


@receiver(post_save, sender=Email)
def send_email(sender, instance, **kwargs):
    def update_group_list(group_list, recipients):
        total_recipients = recipients.count()

        for index in range(0, total_recipients, 1000):
            subgroups = []
            for recipient in recipients[index:index + 1000]:
                subgroups.append(recipient.email)

            group_list.append(subgroups)


@receiver(post_save, sender=Message)
def send_message(sender, instance, **kwargs):
    def filter_mobile_number(mobile):
        mobile_number = mobile.replace("+", '').replace(" ", '').replace("-", '')
        if StringUtils.is_unicode(mobile_number):
            mobile_number = StringUtils.convert_bangla_digit_to_english_digit(mobile_number)
        return "880" + mobile_number[-10:len(mobile_number)]

    def update_group_list(group_list, recipients):
        total_recipients = recipients.count()

        for index in range(0, total_recipients, 50):
            subgroups = []

            for recipient in recipients[index:index + 50]:
                subgroups.append(filter_mobile_number(recipient.mobile))
                group_list.append(subgroups)

    def send(recipients, message):
        sms_kwargs = {'username': settings.SMS_USER, 'api_key': settings.SMS_API_KEY,
                      'sender': settings.SMS_USER, 'receiver': ",".join(recipients), 'message': message}

        sms_url = settings.SMS_API.format(**sms_kwargs)
        requests.get(sms_url)

    group_list = []
    if instance.include_joinus:
        recipients = JoinUs.recipients.valid_recipients(instance)
        update_group_list(group_list, recipients)

    if instance.include_contacts:
        recipients = Contact.recipients.valid_recipients(instance.designation)
        update_group_list(group_list, recipients)

    if instance.mobile:
        subgroups = []
        for _number in filter(None, instance.mobile.split(',')):
            mobile_number = "880" + _number[-10:len(_number)]
            subgroups.append(mobile_number)

        group_list.append(subgroups)

    for group in group_list:
        send(subgroups, instance.text)
