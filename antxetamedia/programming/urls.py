from django.conf.urls import patterns, include, url

from antxetamedia.programming.views import Programming

urlpatterns = patterns('',
        url(r'^$', Programming.as_view(), name='table'),
        )
