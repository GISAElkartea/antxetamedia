from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

from sitemaps import sitemaps
from views import FrontPageView


urlpatterns = patterns('',
        url(r'^$', FrontPageView.as_view(), name='frontpage'),
        (r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

        (r'^programming/', include('programming.urls', namespace='programming')),
        (r'^agenda/', include('agenda.urls', namespace='agenda')),
        (r'^search/', include('search.urls', namespace='search')),
        (r'^multimedia/', include('multimedia.urls', namespace='multimedia')),
        (r'^recordings/', include('recordings.urls')),
        (r'^', include('misc.urls', namespace='misc')),

        (r'^admin/grappelli/', include('grappelli.urls')),
        (r'^admin/', include(admin.site.urls)),
        (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
            url(r'^media/(?P<path>.*)$', 'serve', {
                'document_root': settings.MEDIA_ROOT}, name='media'),
            )

