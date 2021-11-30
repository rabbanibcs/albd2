from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from albd.articles.models import Article


class M100View(TemplateView):
    model = Article
    template_name = 'mujib100/mujib100.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100')

        top_contents = mujib100_articles.filter(position__rank__gte=0).order_by('position__rank')[:5]

        the_liberator = mujib100_articles.filter(sub_category=Article.SUB_CATEGORY.liberator)[:3]
        the_history = mujib100_articles.filter(sub_category=Article.SUB_CATEGORY.history)[:3]
        videos = mujib100_articles.filter(sub_category=Article.SUB_CATEGORY.video)[:5]
        celebrations = mujib100_articles.filter(sub_category=Article.SUB_CATEGORY.celebration)[:2]
        opinions = mujib100_articles.filter(sub_category=Article.SUB_CATEGORY.opinion)[:2]
        context.update(dict(
            top_news=top_contents,
            liberator=the_liberator,
            history=the_history,
            video=videos,
            celebration=celebrations,
            opinions=opinions
        ))

        return context


class M100CelebrationView(TemplateView):
    model = Article
    template_name = 'mujib100/celebration.html'
    item_per_page = 5
    page_counter = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                                       sub_category=Article.SUB_CATEGORY.celebration)
        pages = Paginator(mujib100_articles, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(articles=pages.page(page_number))
        return context


class M100LiberatorView(TemplateView):
    model = Article
    template_name = 'mujib100/liberator.html'
    item_per_page = 5
    page_counter = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                                       sub_category=Article.SUB_CATEGORY.liberator)
        pages = Paginator(mujib100_articles, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(articles=pages.page(page_number))
        return context


class M100HistoryView(TemplateView):
    model = Article
    template_name = 'mujib100/history.html'
    item_per_page = 5
    page_counter = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                                       sub_category=Article.SUB_CATEGORY.history)
        pages = Paginator(mujib100_articles, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(articles=pages.page(page_number))
        return context


class M100VideoView(TemplateView):
    model = Article
    template_name = 'mujib100/video.html'
    item_per_page = 5
    page_counter = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                                       sub_category=Article.SUB_CATEGORY.video)

        pages = Paginator(mujib100_articles, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(articles=pages.page(page_number))
        return context


class M100OpinionView(TemplateView):
    model = Article
    template_name = 'mujib100/opinion.html'
    item_per_page = 5
    page_counter = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mujib100_articles = self.model.on_site.published(exclude_category=None).filter(category__slug='mujib-100',
                                                                                       sub_category=Article.SUB_CATEGORY.opinion)

        pages = Paginator(mujib100_articles, self.item_per_page)
        page_number = self.request.GET.get('page', 1)
        context.update(articles=pages.page(page_number))
        return context
