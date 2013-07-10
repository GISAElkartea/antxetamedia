from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from taggit.models import Tag, TaggedItem

from structure.models import Node
from recordings.models import INTERVIEW
from recordings.models import Program



def context():
    return {
        'latest': Program.objects.filter(type=INTERVIEW).order_by('-pub_date')[:10],
        'tags': TaggedItem.tags_for(Program).filter(program__type=INTERVIEW),
        }


class BaseInterviewList(ListView):
    template_name = 'recordings/interviews/interview_list.html'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        return Program.objects.filter(type=INTERVIEW)

    def get_context_data(self, **kwargs):
        c = super(BaseInterviewList, self).get_context_data(**kwargs)
        c.update(context())
        return c


class NodeInterviewList(BaseInterviewList):
    def get_queryset(self):
        self.node = get_object_or_404(Node, slug=self.kwargs['slug'])
        return super(NodeInterviewList, self).get_queryset().filter(
                program__in=self.node.descendents(including_this=True))

    def get_context_data(self, **kwargs):
        c = super(NodeInterviewList, self).get_context_data(**kwargs)
        c['reason'] = self.node
        return c


class TagInterviewList(BaseInterviewList):
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return super(TagInterviewList, self).get_queryset().filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        c = super(TagInterviewList, self).get_context_data(**kwargs)
        c['reason'] = self.tag
        return c


class InterviewDetail(DetailView):
    template_name = 'recordings/interviews/interview_detail.html'
    queryset = Program.objects.filter(type=INTERVIEW)
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        c = super(InterviewDetail, self).get_context_data(**kwargs)
        c.update(context())
        return c
