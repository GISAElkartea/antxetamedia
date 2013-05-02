from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from taggit.models import Tag, TaggedItem

from structure.models import Node
from recordings.models import Program


def context():
    return {
        'children': Node.objects.children(),
        'latest': Program.objects.order_by('-pub_date')[:10],
        'tags': TaggedItem.tags_for(Program),
        }


class BaseProgramList(ListView):
    template_name = 'recordings/programs/program_list.html'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        c = super(BaseProgramList, self).get_context_data(**kwargs)
        c.update(context())
        return c


class ProgramList(BaseProgramList):
    context_object_name = 'object_list'
    model = Program

    def get_context_data(self, **kwargs):
        c = super(ProgramList, self).get_context_data(**kwargs)
        c['node_list'] = Node.objects.roots()
        return c


class NodeProgramList(BaseProgramList):
    def get_queryset(self):
        self.node = get_object_or_404(Node, slug=self.kwargs['slug'])
        return Program.objects.filter(
                program__in=self.node.descendents(including_this=True))

    def get_context_data(self, **kwargs):
        c = super(NodeProgramList, self).get_context_data(**kwargs)
        c['reason'] = self.node
        c['node_list'] = self.node.children_set.select_related()
        return c


class TagProgramList(BaseProgramList):
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Program.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        c = super(TagProgramList, self).get_context_data(**kwargs)
        c['reason'] = self.tag
        return c


class ProgramDetail(DetailView):
    template_name = 'recordings/programs/program_detail.html'
    model = Program
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        c = super(ProgramDetail, self).get_context_data(**kwargs)
        c.update(context())
        return c
