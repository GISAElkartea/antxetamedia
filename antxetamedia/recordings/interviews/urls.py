from django.conf.urls import patterns, include, url

from antxetamedia.recordings.interviews.feeds import InterviewFeed
from antxetamedia.recordings.interviews.views import (NodeInterviewList,
                                                      InterviewDetail)

urlpatterns = patterns('',
        url(r'^node/(?P<slug>(\w|\d|-)+)/$', NodeInterviewList.as_view(),
            name='node'),
        url(r'^feeds/$', InterviewFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', InterviewDetail.as_view(),
            name='detail'),
        )
