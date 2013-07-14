from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

from antxetamedia.sitemaps import sitemaps
from antxetamedia.views import FrontPageView


urlpatterns = patterns('',
        url(r'^$', FrontPageView.as_view(), name='frontpage'),
        (r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

        (r'^programming/', include('antxetamedia.programming.urls', namespace='programming')),
        (r'^agenda/', include('antxetamedia.agenda.urls', namespace='agenda')),
        (r'^search/', include('antxetamedia.search.urls', namespace='search')),
        (r'^multimedia/', include('antxetamedia.multimedia.urls', namespace='multimedia')),
        (r'^recordings/', include('antxetamedia.recordings.urls')),
        url(r'^projects/', include('antxetamedia.projects.urls', namespace='projects')),
        url(r'^markitup/', include('markitup.urls')),
        (r'^', include('antxetamedia.misc.urls', namespace='misc')),

        (r'^admin/grappelli/', include('grappelli.urls')),
        (r'^admin/', include(admin.site.urls)),
        (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
