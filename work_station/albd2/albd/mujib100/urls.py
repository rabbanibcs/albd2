from django.urls import path

from .views import M100View, M100CelebrationView, M100LiberatorView, M100HistoryView,  M100VideoView, M100OpinionView

app_name = "mujib100"

urlpatterns = [
    path('', M100View.as_view(), name='index'),
    path('celebration/', M100CelebrationView.as_view(), name='celebration'),
    path('liberator/', M100LiberatorView.as_view(), name='liberator'),
    path('history/', M100HistoryView.as_view(), name='history'),
    path('video/', M100VideoView.as_view(), name='video'),
    path('opinion/', M100OpinionView.as_view(), name='opinion')
]
