from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _

from agenda.models import Happening


class HappeningFeed(Feed):
    title = _('Agenda of Antxetamedia')
    link = '/agenda'

    def items(self):
        return Happening.objects.all()

    def item_title(self, obj):
        return obj.__unicode__()

    def item_description(self, obj):
        return obj.description

    def item_link(self, obj):
        return obj.get_absolute_url()

    def item_categories(self, obj):
        return obj.get_town(),
