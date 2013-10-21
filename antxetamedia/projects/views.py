from datetime import date

from django.views.generic import ListView, DetailView, YearArchiveView

from antxetamedia.projects.models import Project


class ProjectList(ListView):
    template_name = 'projects/project_list.html'
    allow_empty = True

    def get_queryset(self):
        return Project.objects.filter(beginning__year=date.today().year)

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectList, self).get_context_data(*args, **kwargs)
        context['years'] = Project.objects.dates('beginning', 'year')
        return context


class YearProjectList(YearArchiveView):
    date_field = 'beginning'
    make_object_list = True
    model = Project
    template_name = 'projects/project_list.html'
    allow_empty = True


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    slug_field = 'slug'
