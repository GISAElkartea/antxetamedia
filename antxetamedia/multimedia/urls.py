from django.conf.urls import patterns, include, url

from antxetamedia.multimedia.views import OrphanedMediaList


urlpatterns = patterns('',
        url(r'^$', OrphanedMediaList.as_view(), name='view'),
        )
