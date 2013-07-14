from haystack import indexes

from antxetamedia.agenda.models import Happening


class HappeningIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexable.CharField(document=True, use_template=True)

    name = indexable.CharField(model_attr='name')
    organizer = indexable.CharField(model_attr='organizer')
    description = indexable.CharField(model_attr='description')
    date = indexable.DateField(model_attr='date')
    town = indexable.CharField()
    place = indexable.CharField(model_attr='place')

    def prepare_town(self, obj):
        if obj.town:
            return obj.town
        return obj.other_town

    def get_model(self):
        return Happening
