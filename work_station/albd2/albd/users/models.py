from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from djchoices import DjangoChoices, ChoiceItem


class User(AbstractUser):
    """Default user for Bangladesh Awamileague."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Gender(DjangoChoices):
    Male = ChoiceItem('M')
    Female = ChoiceItem('F')
    Others = ChoiceItem('O')
