from django.conf.urls import url, include
from django.contrib.staticfiles.views import serve
from django.conf import settings
from .views import urlpatterns


urlpatterns = [
    url(r'^api/', include(urlpatterns)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'', serve, kwargs={'path': 'index.html'}),
    ]
