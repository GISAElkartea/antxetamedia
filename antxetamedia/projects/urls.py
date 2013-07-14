from django.conf.urls import patterns, include, url

from antxetamedia.projects.views import ProjectList, ProjectDetail

urlpatterns = patterns('',
        url(r'^$', ProjectList.as_view(), name='list'),
        url(r'^(?P<slug>(\w|\d|-)+)/$', ProjectDetail.as_view(), name='detail'),
        )
