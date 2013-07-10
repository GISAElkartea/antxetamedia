from django.conf.urls.defaults import *

from recordings.programs.feeds import ProgramFeed
from recordings.programs.views import ProgramList, NodeProgramList, \
        TagProgramList, ProgramDetail


urlpatterns = patterns('',
        url(r'^$', ProgramList.as_view(), name='list'),
        url(r'^node/(?P<slug>(\w|\d|-)+)/$', NodeProgramList.as_view(),
            name='node'),
        url(r'^tag/(?P<slug>(\w|\d|-)+)/$', TagProgramList.as_view(),
            name='tag'),
        url(r'^feeds/$', ProgramFeed(), name='feed'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', ProgramDetail.as_view(), 
            name='detail'),
        )
