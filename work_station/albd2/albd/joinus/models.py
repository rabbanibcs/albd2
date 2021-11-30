from django.db import models
from django.utils.translation import ugettext_lazy as _

from albd.users.models import Gender


class Division(models.Model):
    name = models.CharField(_("Name"), blank=False, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE, related_name='districts', blank=True, null=True)

    name = models.CharField(_("Name"), blank=False, max_length=100)
    code = models.CharField(blank=True, null=True, max_length=10)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Constituency(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name='constituencies', blank=True, null=True)

    name = models.CharField(_("Name"), blank=False, max_length=100)
    code = models.CharField(blank=True, null=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Constituency'
        verbose_name_plural = 'Constituencies'

    def __str__(self):
        return self.name


class RecipientsManager(models.Manager):

    def valid_recipients(self, msg_instance, preference="2"):

        qs = self.get_queryset().filter(preference__contains=preference)

        if msg_instance.division:
            qs = qs.filter(division=msg_instance.division)

        if msg_instance.district:
            qs = qs.filter(district=msg_instance.district)

        if msg_instance.constituency:
            qs = qs.filter(constituency=msg_instance.constituency)

        return qs


class JoinUs(models.Model):
    full_name = models.CharField(_("Full Name"), blank=False, max_length=255)
    gender = models.CharField(_("Gender"), blank=False, choices=Gender.choices, max_length=10)
    dob = models.DateField(_("Date of Birth"), blank=False)
    mobile = models.CharField(_("Mobile"), blank=False, max_length=13)
    email = models.EmailField(_("Email"), blank=False)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, related_name='members', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, related_name='members', blank=True, null=True)
    constituency = models.ForeignKey(Constituency, on_delete=models.SET_NULL, related_name='members', blank=True, null=True)
    preference = models.CharField(blank=False, max_length=10)
    join_date = models.DateTimeField(auto_now_add=True)

    recipients = RecipientsManager()

    class Meta:
        verbose_name = "Join Us"
        verbose_name_plural = "Join Us"
