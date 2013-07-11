from haystack.indexes import *
from haystack import site

from antxetamedia.agenda.models import Happening


class HappeningIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    name = CharField(model_attr='name')
    organizer = CharField(model_attr='organizer')
    description = CharField(model_attr='description')
    date = DateField(model_attr='date')
    town = CharField()
    place = CharField(model_attr='place')

    def prepare_town(self, obj):
        if obj.town:
            return obj.town
        return obj.other_town

site.register(Happening, HappeningIndex)
