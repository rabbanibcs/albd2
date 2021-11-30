from django import forms
from django.utils.translation import ugettext_lazy as _
from datetime import date
from django.forms import widgets

from .models import JoinUs, Division, District, Constituency

CHECKBOX_CHOICES = (('1', _("Email")), ('2', _("Phone")))


class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        years = [(year, year) for year in range(1920, 2020)]
        months = [(month, month) for month in range(1, 12)]
        days = [(day, day) for day in range(1, 31)]

        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(
                day=int(datelist[0]),
                month=int(datelist[1]),
                year=int(datelist[2]),
            )
        except ValueError:
            return ''
        else:
            return str(D)


def clean_unique(form, field, exclude_initial=True,
                 format=_("The %(field)s %(value)s has already been taken.")):
    value = form.cleaned_data.get(field)
    if value:
        qs = form._meta.model._default_manager.filter(**{field: value})
        if exclude_initial and form.initial:
            initial_value = form.initial.get(field)
            qs = qs.exclude(**{field: initial_value})
        if qs.count() > 0:
            raise forms.ValidationError(format % {'field': field, 'value': value})
    return value


class JoinUsForm(forms.ModelForm):
    division = forms.ModelChoiceField(
        queryset=Division.objects.all(), required=True, empty_label=_("Please select a division"))

    district = forms.ModelChoiceField(
        empty_label=_("Select a District"),
        queryset=District.objects.all(), required=True,
    )
    constituency = forms.ModelChoiceField(
        empty_label=_("Select a Constituency"),
        queryset=Constituency.objects.all(), required=True,
    )
    preference = forms.MultipleChoiceField(
        required=True, widget=widgets.CheckboxSelectMultiple, choices=CHECKBOX_CHOICES)

    class Meta:
        model = JoinUs
        fields = ('full_name', 'gender', 'dob', 'mobile', 'email', 'division', 'district', 'constituency', 'preference')

        widgets = {
            'dob': widgets.DateInput(attrs={"class": "datepicker"})
        }
        help_texts = {
            'mobile': 'Please enter 11 digits of your phone number e.g: 017xxxxxxxx',
        }

    def clean_mobile(self):
        return clean_unique(self, 'mobile')

    def clean_email(self):
        return clean_unique(self, 'email')


class JoinUsAdminForm(forms.ModelForm):
    preference = forms.MultipleChoiceField(
        required=True, widget=widgets.CheckboxSelectMultiple, choices=CHECKBOX_CHOICES)

    class Meta:
        model = JoinUs
        fields = ('full_name', 'gender', 'dob', 'mobile', 'email', 'division', 'district', 'constituency', 'preference')
