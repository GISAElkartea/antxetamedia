from django.contrib import admin
from django.utils.translation import ugettext as _

from antxetamedia.projects.models import Project
from antxetamedia.tools import admin_image


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'img']
    img = admin_image('image')

admin.site.register(Project, ProjectAdmin)
