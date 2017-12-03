from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.http import JsonResponse


def index(request):
    return JsonResponse({"Hello": "World"})


urlpatterns = [
    url(r'^api/hello_world', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'', serve, kwargs={'path': 'index.html'}),
        url(r'^(?P<path>.*\..*)$', RedirectView.as_view(url='/static/%(path)s', permanent=False))
    ]
