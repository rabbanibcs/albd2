from django.urls import path
from django.views.generic import TemplateView

from .views import AjaxChainedDistricts, AjaxChainedConstituencies

app_name = "joinus"

urlpatterns = [
    path("districts/", view=AjaxChainedDistricts.as_view(), name='ajax_chained_districts'),
    path("constituencies/", view=AjaxChainedConstituencies.as_view(), name='ajax_chained_constituencies'),
    path("thank-you/", view=TemplateView.as_view(template_name='joinus/thank-you.html'), name='thanks')
]
