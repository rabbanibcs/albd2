from django.views.generic.edit import FormView

from clever_selects.views import ChainedSelectChoicesView

from .forms import JoinUsForm
from .models import District, Constituency


class JoinUsView(FormView):
    form_class = JoinUsForm

    def get_success_url(self):
        from django.urls import reverse  # noqa
        return reverse('joinus:thanks')

    def form_valid(self, form):
        form = form.save()

        return super().form_valid(form)


class AjaxChainedDistricts(ChainedSelectChoicesView):
    def get_child_set(self):
        return District.objects.filter(division_id=self.parent_value)


class AjaxChainedConstituencies(ChainedSelectChoicesView):
    def get_child_set(self):
        return Constituency.objects.filter(district_id=self.parent_value)
