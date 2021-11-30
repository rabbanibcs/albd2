# -*- coding: utf-8 -*-

import re
import urllib
import math
import difflib
from django.utils.deprecation import MiddlewareMixin
from djchoices import DjangoChoices, ChoiceItem


class FixRemoteIPMiddleware(MiddlewareMixin):

    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = str(x_forwarded_for.split(',')[0])
        else:
            ip = '1.1.1.1'

        request.META['REMOTE_ADDR'] = ip


class StringUtils(object):
    bn_numbers = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
    en_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    uc_pattern = re.compile("[^\x00-\x7F]")
    extended_gsm_chars = "~^{}[]\|€"
    unicode = 0
    count = 0

    def __init__(self, msg):
        self.message = msg
        self.type = "plaintext"

    def qoute_plus(self):
        return urllib.quote_plus(self.message.encode('utf-8') or '')

    def hexify(self):
        return "".join(["%04x" % ord(ch) for ch in self.message])

    def get_type(self, message):

        if self.uc_pattern.search(message):
            sms_type = "unicode"
            self.unicode = 1
            return sms_type

        matcher = difflib.SequenceMatcher(a=message, b=self.extended_gsm_chars)
        match = matcher.find_longest_match(0, len(matcher.a), 0, len(matcher.b))

        if match.size > 1:
            sms_type = "gsm_extended"
            return sms_type

        sms_type = 'plaintext'
        return sms_type

    def get_count(self, nchar):

        self.type = self.get_type(self.message)

        if self.type == "unicode":
            self.unicode = 1
            if nchar <= 70:
                no_of_sms = 1
            else:
                actualSMSLength = 70 - 3
                no_of_sms = math.ceil(float(nchar) / actualSMSLength)

        elif self.type == "gsm_extended":
            if nchar <= 140:
                no_of_sms = 1
            else:
                actualSMSLength = 140 - 6
                no_of_sms = math.ceil(float(nchar) / actualSMSLength)
        else:
            if nchar <= 160:
                no_of_sms = 1
            else:
                actualSMSLength = 160 - 7
                no_of_sms = math.ceil(float(nchar) / actualSMSLength)

        self.count = no_of_sms
        return no_of_sms

    @classmethod
    def is_unicode(cls, string):
        if cls.uc_pattern.search(string):
            return True
        else:
            return False

    @classmethod
    def convert_bangla_digit_to_english_digit(cls, original):
        converted = ""
        for character in str(original):
            if character in cls.bn_numbers:
                converted += cls.en_numbers[cls.bn_numbers.index(character)]
            else:
                converted += character
        return converted


class Languages(DjangoChoices):
    English = ChoiceItem('en')
    Bangla = ChoiceItem('bn')
