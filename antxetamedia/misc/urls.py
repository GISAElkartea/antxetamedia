from django.conf.urls import patterns, include, url

from antxetamedia.misc.views import AboutUsView


urlpatterns = patterns('',
        url(r'^about_us/$', AboutUsView.as_view(), name='aboutus'),
)
