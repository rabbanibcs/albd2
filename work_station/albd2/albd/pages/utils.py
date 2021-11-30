from .models import Page


def get_category_page_titles():
    return Page.on_site.published().all()
