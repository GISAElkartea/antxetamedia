from django.conf.urls.defaults import *


urlpatterns = patterns('',
        (r'^news/', include('recordings.news.urls',
            namespace='news')),
        (r'^interviews/', include('recordings.interviews.urls',
            namespace='interviews')),
        (r'^programs/', include('recordings.programs.urls',
            namespace='programs')),
)
