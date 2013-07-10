from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from taggit.models import Tag, TaggedItem

from recordings.models import News, NewsCategory


def context():
    return {
        'latest': News.objects.order_by('-pub_date')[:10],
        'tags': TaggedItem.tags_for(News),
        }


class BaseNewsList(ListView):
    template_name = 'recordings/news/news_list.html'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        c = super(BaseNewsList, self).get_context_data(**kwargs)
        c.update(context())
        return c


class NewsList(BaseNewsList):
    model = News
    context_object_name = 'object_list'


class CategoryNewsList(BaseNewsList):
    def get_queryset(self):
        self.category = get_object_or_404(NewsCategory, slug=self.kwargs['slug'])
        return News.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        c = super(CategoryNewsList, self).get_context_data(**kwargs)
        c['reason'] = self.category
        return c


class TagNewsList(BaseNewsList):
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return News.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        c = super(TagNewsList, self).get_context_data(**kwargs)
        c['reason'] = self.tag
        return c


class NewsDetail(DetailView):
    template_name = 'recordings/news/news_detail.html'
    model = News
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        c = super(NewsDetail, self).get_context_data(**kwargs)
        c.update(context())
        return c
