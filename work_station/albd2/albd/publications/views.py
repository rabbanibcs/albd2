from django.views.generic import TemplateView

from .models import Publication


class PublicationView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(publications=Publication.objects.published().all())
        return context
