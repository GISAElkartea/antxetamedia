from haystack import indexes

from antxetamedia.agenda.models import Happening


class HappeningIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    name = indexes.CharField(model_attr='name')
    organizer = indexes.CharField(model_attr='organizer')
    description = indexes.CharField(model_attr='description')
    date = indexes.DateField(model_attr='date')
    town = indexes.CharField()
    place = indexes.CharField(model_attr='place')

    def prepare_town(self, obj):
        if obj.town:
            return obj.town
        return obj.other_town

    def get_model(self):
        return Happening
