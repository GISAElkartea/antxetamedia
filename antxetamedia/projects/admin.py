from django.contrib import admin
from django.utils.translation import ugettext as _

from antxetamedia.projects.models import Project
from antxetamedia.tools import admin_image
from antxetamedia.multimedia.admin import (MediaRelated, MediaInline,
                                           EmbededMediaInline)


class ProjectAdmin(MediaRelated):
    fields = (('name', 'beginning'), 'text', 'aside', 'image')
    list_display = ['name', 'beginning', 'img']
    img = admin_image('image')
    inlines = MediaInline, EmbededMediaInline

admin.site.register(Project, ProjectAdmin)
