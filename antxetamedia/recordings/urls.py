from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
        (r'^news/', include('antxetamedia.recordings.news.urls',
            namespace='news')),
        (r'^interviews/', include('antxetamedia.recordings.interviews.urls',
            namespace='interviews')),
        (r'^programs/', include('antxetamedia.recordings.programs.urls',
            namespace='programs')),
)
