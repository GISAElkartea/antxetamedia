from django.conf.urls.defaults import *

from antxetamedia.programming.views import Programming

urlpatterns = patterns('',
        url(r'^$', Programming.as_view(), name='table'),
        )
