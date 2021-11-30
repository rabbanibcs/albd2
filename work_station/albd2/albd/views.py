from django.views.generic.base import TemplateView
from albd.articles.models import Article
from albd.publications.models import Publication
from albd.gallery.models import Gallery


class HomePageView(TemplateView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publications = Publication.objects.published()
        top_news = self.model.on_site.get_top_news(limit=5)
        gallery = self.model.on_site.get_article_items(category_name='gallery', limit=10)

        # Publications
        total_publications = publications.count()
        all_publications = []

        for index in range(0, total_publications, 3):
            all_publications.append(publications[index:index + 3])

        view_opinions = self.model.on_site.get_article_items(category_name='views-opinion', limit=5)
        news = self.model.on_site.get_article_items(category_name='news', limit=5)
        party_news = self.model.on_site.get_article_items(category_name='party-news', limit=5)

        # Views and opinions
        total_views = view_opinions.count()
        all_views_opinions = []

        for index in range(0, total_views, 2):
            all_views_opinions.append(view_opinions[index:index + 2])

        gallery_video = Gallery.objects.published().filter(type__exact='video').first()
        gallery_live = Gallery.objects.published().filter(type__exact='live').first()
        gallery_info = Gallery.objects.published().filter(type__exact='info').first()
        gallery_history = Gallery.objects.published().filter(type__exact='history').first()

        context.update({
            'top_news': top_news,
            'gallery': gallery,
            'view_opinions': all_views_opinions,
            'publications': all_publications,
            'gallery_video': gallery_video,
            'gallery_info': gallery_info,
            'gallery_history': gallery_history,
            'gallery_live': gallery_live,
            'news': news,
            'party_news': party_news
        })

        return context


class GalleryView(TemplateView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.model.on_site.get_gallery_items(content_type='photo')
        videos = self.model.on_site.get_gallery_items(content_type='video')

        context.update(dict(photos=photos, videos=videos))

        return context
