from django.urls import path

from .views import CategoryDetailView, CategoryItemView, ContentTypeItemView

app_name = "categories"

urlpatterns = [
    path('<str:slug>', view=CategoryDetailView.as_view(), name='detail'),
    path('<str:slug>/items/', CategoryItemView.as_view(), name='items'),
    path('<str:content_type>/contents/', ContentTypeItemView.as_view(), name='typed_items'),
]
