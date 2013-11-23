from django.conf.urls import patterns, include, url

from antxetamedia.recordings.news.feeds import NewsFeed
from antxetamedia.recordings.news.views import (NewsList, CategoryNewsList,
                                                NewsDetail)


urlpatterns = patterns('',
        url(r'^$', NewsList.as_view(), name='list'),
        url(r'^category/(?P<slug>(\w|\d|-)+)/$', CategoryNewsList.as_view(),
            name='category'),
        url(r'^feeds/$', NewsFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', NewsDetail.as_view(),
            name='detail'),
        )
