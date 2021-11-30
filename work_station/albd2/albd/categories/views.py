from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.utils.translation import get_language
from albd.categories.models import Category
from albd.articles.models import Article


class CategoryDetailView(DetailView):
    model = Category
    slug_field = 'slug'
    query_pk_and_slug = True
    item_per_page = 5
    page_counter = 18

    def get_template_names(self):
        template_prefix = "news"
        if self.object.slug == 'gallery' or self.object.slug == 'decade-of-development':
            template_prefix = "{}".format(self.object.slug)

        template_name = "categories/{}_detail.html".format(template_prefix)

        return [template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'label_title': self.object.label})
        lang = get_language()
        objects = context['object'].articles.get_queryset().filter(lang=lang)

        if context['object'].slug == 'decade-of-development':
            context.update(page=objects.all())
        else:
            pages = Paginator(objects, self.item_per_page)
            page_number = self.request.GET.get('page', 1)
            context.update(page=pages.page(page_number))

        if context['object'].slug == 'gallery':
            videos = objects.filter(content_type__slug='video').all()
            photos = objects.filter(content_type__slug='photo').all()
            context.update(dict(photos=photos, videos=videos))

        return context


class CategoryItemView(DetailView):
    model = Category
    slug_field = 'slug'
    query_pk_and_slug = True
    limit = 4

    def get_template_names(self):
        template_name = "categories/category_items.html"
        return [template_name]

    def get_context_data(self, **kwargs):
        lang = get_language()
        context = super().get_context_data(**kwargs)
        limit = int(self.request.GET.get('limit', self.limit))
        context.update({'label_title': self.object.label})
        objects = context['object'].articles.get_queryset().filter(lang=lang)
        context.update(items=objects.all()[:limit])
        return context


class ContentTypeItemView(TemplateView):
    model = Article
    template_name = "categories/content_type_items.html"
    limit = 5

    def get_context_data(self, **kwargs):
        limit = int(self.request.GET.get('limit', self.limit))
        content_type = self.kwargs.get('content_type')
        context = super().get_context_data(**kwargs)
        content = self.model.on_site.published().filter(content_type__slug=content_type)[:limit]
        context.update({'items': content})
        return context
