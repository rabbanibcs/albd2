from django.urls import path

from .views import ArticleDetailView, TaggableArticleListView, CategoryWiseArticleListView, ContentTypeArticleView

app_name = "articles"

urlpatterns = [
    path("<str:content_type>/<int:article_id>/<str:slug>", view=ArticleDetailView.as_view(), name='detail'),
    path("<str:content_type>/<int:article_id>/", view=ArticleDetailView.as_view(), name='detail-on-id'),
    path("<str:category_slug>/", view=CategoryWiseArticleListView.as_view(), name='category-wise-articles'),
    path("taggit/<str:slug>", view=TaggableArticleListView.as_view(), name='taggit_articles'),
    path("<str:content_type>/contents/", ContentTypeArticleView.as_view(), name='content-type-articles')
]
