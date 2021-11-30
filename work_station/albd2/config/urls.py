from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

from rest_framework.authtoken.views import obtain_auth_token
from albd.views import HomePageView
from albd import search
from albd.newsletters.views import NewsletterView
from albd.joinus.views import JoinUsView
from albd.publications.views import PublicationView

urlpatterns = i18n_patterns(
    path("", HomePageView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("register/", JoinUsView.as_view(template_name='pages/join_us.html'), name='register'),
    path('livetv/', TemplateView.as_view(template_name='pages/livetv.html'), name='livetv'),
    path('mps/', TemplateView.as_view(template_name='pages/mps.html'), name='mps'),
    path('president/', TemplateView.as_view(template_name='pages/president.html'), name='president'),
    path('publications/', PublicationView.as_view(template_name='pages/publications.html'), name='publications'),
    path('newsletter/', NewsletterView.as_view(template_name='pages/newsletter.html'), name='newsletter'),
    path('download/', TemplateView.as_view(template_name='pages/download.html'), name='download'),
    path('timelines/', TemplateView.as_view(template_name='pages/timelines.html'), name='timelines'),
    path('contact-us/', TemplateView.as_view(template_name='pages/about.html'), name='contact-us'),
    path('article-search/', search.Search.as_view(template_name='pages/search_result.html'), name='search'),
    path('mujib100/', include('albd.mujib100.urls', namespace='mujib100')),
    # Your stuff: custom urls includes go here
    path('articles/', include('albd.articles.urls', namespace='articles')),
    path('pages/', include('albd.pages.urls', namespace='pages')),
    path('category/', include('albd.categories.urls', namespace='categories')),
    # path('members/login/', UserLoginView.as_view(), name="custom_account_login"),
    # User management
    path("users/", include("albd.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    prefix_default_language=False
)

urlpatterns += [ path('i18n/', include('django.conf.urls.i18n')) ]

urlpatterns += [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('joinus/', include('albd.joinus.urls', namespace='joinus')),
    path('comments/', include('django_comments.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
