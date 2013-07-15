from antxetamedia.projects.models import Project

def projects(request):
    return {'project_list': Project.objects.all()}
