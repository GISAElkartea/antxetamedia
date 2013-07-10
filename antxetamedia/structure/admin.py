from django.contrib import admin
from django.utils.translation import gettext as _

from structure.models import Node
from structure.forms import NodeForm
from tools import admin_image

class NodeAdmin(admin.ModelAdmin):
    form = NodeForm
    list_display = 'name', 'parent', 'on_menu', 'on_frontpage', 'img'
    list_filter = 'on_menu', 'on_frontpage'
    img = admin_image('image')

    fieldsets = (
            (None, {
                'fields': (('name', 'on_menu', 'on_frontpage'), 'parent')}),
            (_('Details'), {
                'fields': ('description', 'link', 'image')}),
            )
admin.site.register(Node, NodeAdmin)
