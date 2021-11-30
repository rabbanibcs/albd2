from django.urls import path
from .views import PageListView, PageDetailView, CustomDetailView

app_name = "pages"

urlpatterns = [
    path('<str:slug>', PageDetailView.as_view(), name='detail'),
    path('<int:page_id>/<str:slug>', CustomDetailView.as_view(), name='custom-detail'),
    path('', PageListView.as_view(), name='list'),
]
