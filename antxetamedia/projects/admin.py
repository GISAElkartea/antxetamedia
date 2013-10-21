from django.contrib import admin
from django.utils.translation import ugettext as _

from antxetamedia.projects.models import Project
from antxetamedia.tools import admin_image
from antxetamedia.multimedia.admin import (MediaRelated, MediaInline,
                                           EmbededMediaInline)


class ProjectAdmin(MediaRelated):
    list_display = ['name', 'img']
    img = admin_image('image')
    inlines = MediaInline, EmbededMediaInline

admin.site.register(Project, ProjectAdmin)
