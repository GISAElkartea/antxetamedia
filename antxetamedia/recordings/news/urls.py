from django.conf.urls.defaults import *

from recordings.news.feeds import NewsFeed
from recordings.news.views import NewsList, CategoryNewsList, TagNewsList,\
        NewsDetail


urlpatterns = patterns('',
        url(r'^$', NewsList.as_view(), name='list'),
        url(r'^category/(?P<slug>(\w|\d|-)+)/$', CategoryNewsList.as_view(),
            name='category'),
        url(r'^tag/(?P<slug>(\w|\d|-)+)/$', TagNewsList.as_view(),
            name='tag'),
        url(r'^feeds/$', NewsFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', NewsDetail.as_view(), 
            name='detail'),
        )
