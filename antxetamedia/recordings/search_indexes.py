from haystack import indexes

from antxetamedia.recordings.models import News, Program


class RecordingIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title')
    date = indexes.CharField(model_attr='pub_date')
    body = indexes.CharField(model_attr='text')
    

class NewsIndex(RecordingIndex, indexes.Indexable):
    categories = indexes.MultiValueField()

    def prepare_categories(self, obj):
        return [category.id for category in obj.categories.all()]

    def get_model(self):
        return News


class ProgramIndex(RecordingIndex, indexes.Indexable):
    program = indexes.CharField(model_attr='program')

    def get_model(self):
        return Program
