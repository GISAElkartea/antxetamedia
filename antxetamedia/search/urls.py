from django.conf.urls.defaults import *

from haystack.views import search_view_factory

from antxetamedia.search.views import SearchView

urlpatterns = patterns('',
        url(r'^$', search_view_factory(view_class=SearchView), name='search'),
)
