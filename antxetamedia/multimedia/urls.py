from django.conf.urls.defaults import *

from multimedia.views import OrphanedMediaList


urlpatterns = patterns('',
        url(r'^$', OrphanedMediaList.as_view(), name='view'),
        )
