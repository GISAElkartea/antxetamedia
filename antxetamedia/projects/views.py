from django.views.generic import ListView, DetailView

from antxetamedia.projects.models import Project


class ProjectList(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    allow_empty = True


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    slug_field = 'slug'
