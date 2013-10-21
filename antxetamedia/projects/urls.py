from django.conf.urls import patterns, include, url

from antxetamedia.projects.views import (ProjectList, YearProjectList,
                                         ProjectDetail)

urlpatterns = patterns('',
        url(r'^$', ProjectList.as_view(), name='list'),
        url(r'^(?P<year>\d+)/$', YearProjectList.as_view(), name='year'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', ProjectDetail.as_view(), name='detail'),
        )
