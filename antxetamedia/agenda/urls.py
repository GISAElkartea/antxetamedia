from django.conf.urls.defaults import *

from agenda.feeds import HappeningFeed
from agenda.views import FutureHappeningList, OtherTownHappeningList, \
        TownHappeningList, DayHappeningList, HappeningDetail, \
        CreateHappening, SuccessfulCreate


urlpatterns = patterns('',
        url(r'^$', FutureHappeningList.as_view(), name='list'),
        url(r'^other_town/$', OtherTownHappeningList.as_view(), name='other_town'),
        url(r'^town/(?P<slug>(\d|\w|-)+)/$', TownHappeningList.as_view(),
            name='town'),
        url(r'^day/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
            DayHappeningList.as_view(), name='day'),

        url(r'^create/$', CreateHappening.as_view(), name='create'),
        url(r'^create/success/$', SuccessfulCreate.as_view(), name='success'),
        url(r'^feeds/$', HappeningFeed(), name='feed'),
        url(r'^(?P<slug>(\d|\w|-)+)/$', HappeningDetail.as_view(), 
            name='detail'),
        )
