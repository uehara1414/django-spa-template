from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.http import JsonResponse
from .views import urlpatterns


def index(request):
    return JsonResponse({"Hello": "World"})


urlpatterns = [
    url(r'^api/', include(urlpatterns)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'', serve, kwargs={'path': 'index.html'}),
        url(r'^(?P<path>.*\..*)$', RedirectView.as_view(url='/static/%(path)s', permanent=False))
    ]
