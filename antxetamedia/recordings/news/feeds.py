from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _

from datetime import datetime, time

from antxetamedia.recordings.models import News


class NewsFeed(Feed):
    title = _('News of Antxetamedia')
    link = '/recordings/news'

    def items(self):
        return News.objects.all()

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return obj.text

    def item_link(self, obj):
        return obj.get_absolute_url()

    def item_pubdate(self, obj):
        return datetime.combine(obj.pub_date, time(0, 0))

    def item_categories(self, obj):
        return obj.categories.all()
