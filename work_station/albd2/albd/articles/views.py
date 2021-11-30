from django.core.paginator import Paginator
from django.utils import timezone
from django.utils.translation import get_language
# from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView

from albd.livetv.models import LiveTV
from .models import Article
from albd.categories.models import Category


class ArticleDetailView(HitCountDetailView):
    model = Article
    count_hit = True
    pk_url_kwarg = 'article_id'
    query_pk_and_slug = False

    def get_queryset(self):
        lang = get_language()
        return super().get_queryset().filter(lang=lang)

    def get_template_names(self):
        template_prefix = "article"

        if self.object.category.slug in ['gallery', 'mujib-100'] and \
                self.object.content_type.slug in ['photo', 'video']:
            template_prefix = "{}".format(self.object.content_type.slug)

        template_dir = "articles"

        if self.object.category.slug == 'mujib-100':
            template_dir = 'mujib100'

        template_name = "{}/{}_detail.html".format(template_dir, template_prefix)
        return [template_name]


class CategoryWiseArticleListView(ListView):
    model = Article
    item_per_page = 20
    template_name = 'categories/news_detail.html'

    def get_context_data(self, **kwargs):
        lang = get_language()
        context = super().get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['category_slug']).first()
        if category:
            context.update({'label_title': category.label})
        qs = Article.objects.filter(category__slug=self.kwargs['category_slug']).filter(lang=lang)
        pages = Paginator(qs, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(page=pages.page(page_number))
        return context


class TaggableArticleListView(ListView):
    paginate_by = 20
    template_name = 'categories/news_detail.html'

    def get_queryset(self):
        lang = get_language()
        return Article.objects.filter(lang=lang)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset().filter(tags__slug=self.kwargs['slug'])
        pages = Paginator(qs, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        context.update(page=pages.page(page_number))
        return context


class ContentTypeArticleView(ListView):
    model = Article
    item_per_page = 20

    def get_template_names(self):
        template_name = "categories/gallery_{}_detail.html".format(self.kwargs.get('content_type'))
        return [template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Article.on_site.published().filter(content_type__slug=self.kwargs.get('content_type'))
        context.update({'items': qs.all()})
        return context

