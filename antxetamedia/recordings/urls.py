from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^news/', include('antxetamedia.recordings.news.urls',
            namespace='news')),
        (r'^interviews/', include('antxetamedia.recordings.interviews.urls',
            namespace='interviews')),
        (r'^programs/', include('antxetamedia.recordings.programs.urls',
            namespace='programs')),
)
