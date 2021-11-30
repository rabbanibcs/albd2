from django.db import models
from django.utils.translation import ugettext_lazy as _


class Designation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ContactsManager(models.Manager):

    def valid_recipients(self, designation=None):
        if not designation:
            return self.get_queryset()

        return self.get_queryset().filter(designation=designation)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="contact_list")
    mobile = models.CharField(_("Mobile"), blank=False, max_length=13)
    email = models.EmailField(_("Email"), blank=False)
    recipients = ContactsManager()

    def __str__(self):
        return self.name
