from django.conf.urls.defaults import *

from misc.views import AboutUsView


urlpatterns = patterns('',
        url(r'^about_us/$', AboutUsView.as_view(), name='aboutus'),
)
