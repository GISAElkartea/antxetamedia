from haystack.indexes import *
from haystack import site

from antxetamedia.recordings.models import News, Program

class RecordingIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    title = CharField(model_attr='title')
    date = CharField(model_attr='pub_date')
    body = CharField(model_attr='text')
    

class NewsIndex(RecordingIndex):
    categories = MultiValueField()

    def prepare_categories(self, obj):
        return [category.id for category in obj.categories.all()]


class ProgramIndex(RecordingIndex):
    program = CharField(model_attr='program')


site.register(News, NewsIndex)
site.register(Program, ProgramIndex)
