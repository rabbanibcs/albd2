from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from django.utils.translation import get_language
from django.views.generic import ListView

from albd.articles.models import Article


class Search(ListView):
    item_per_page = 10

    def get_queryset(self):
        lang = get_language()

        q = self.request.GET.get('q')
        return Article.objects.annotate(
            search=SearchVector('title', 'short_title', 'body'),
        ).filter(lang=lang).filter(search=q)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pages = Paginator(self.get_queryset(), self.item_per_page)
        page_number = self.request.GET.get('page', 1)

        context.update({
            'articles': pages.page(page_number),
            'total_count': pages.count,
            'q': self.request.GET.get('q')
        })

        return context
