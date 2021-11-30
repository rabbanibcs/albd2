from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from .models import Gender

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class SignupForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(required=True, min_length=10, max_length=13)
    nationality = LazyTypedChoiceField(choices=countries)
    gender = forms.ChoiceField(choices=Gender.choices)

    class Meta:
        model = User
        fields = ('name', 'phone', 'nationality', 'gender')

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            self.add_error('phone', _("This phone number is already exists!"))

    def signup(self, request, user):
        user.phone = self.cleaned_data.get('phone')
        user.name = self.cleaned_data.get('name')

        user.save()
