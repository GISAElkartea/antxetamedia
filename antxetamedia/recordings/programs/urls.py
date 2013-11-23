from django.conf.urls import patterns, include, url

from antxetamedia.recordings.programs.feeds import ProgramFeed
from antxetamedia.recordings.programs.views import (ProgramList,
                                                    NodeProgramList,
                                                    ProgramDetail)


urlpatterns = patterns('',
        url(r'^$', ProgramList.as_view(), name='list'),
        url(r'^node/(?P<slug>(\w|\d|-)+)/$', NodeProgramList.as_view(),
            name='node'),
        url(r'^feeds/$', ProgramFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', ProgramDetail.as_view(),
            name='detail'),
        )
