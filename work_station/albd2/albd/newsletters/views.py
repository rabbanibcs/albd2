from django.views.generic import TemplateView

from .models import Newsletter


class NewsletterView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(newsletters=Newsletter.objects.get_published().all())
        return context
