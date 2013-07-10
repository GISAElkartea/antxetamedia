from django.conf.urls.defaults import *

from recordings.interviews.feeds import InterviewFeed
from recordings.interviews.views import NodeInterviewList, TagInterviewList,\
        InterviewDetail

urlpatterns = patterns('',
        url(r'^node/(?P<slug>(\w|\d|-)+)/$', NodeInterviewList.as_view(),
            name='node'),
        url(r'^tag/(?P<slug>(\w|\d|-)+)/$', TagInterviewList.as_view(),
            name='tag'),
        url(r'^feeds/$', InterviewFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', InterviewDetail.as_view(), 
            name='detail'),
        )
