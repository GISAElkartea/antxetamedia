from django.conf.urls.defaults import *

from programming.views import Programming

urlpatterns = patterns('',
        url(r'^$', Programming.as_view(), name='table'),
        )
