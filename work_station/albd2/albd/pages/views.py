from django.shortcuts import render
from django.utils.translation import get_language

from django.views.generic.list import ListView, InvalidPage
from django.views.generic.detail import DetailView

from .models import Page


class PageListView(ListView):
    pass


class PageDetailView(DetailView):
    model = Page
    slug_field = 'slug'
    query_pk_and_slug = True


class CustomDetailView(DetailView):
    model = Page
    pk_url_kwarg = 'page_id'
    query_pk_and_slug = False

    def get_queryset(self):
        lang = get_language()
        return super().get_queryset().filter(lang=lang)
