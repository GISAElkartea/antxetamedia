from django.contrib import admin
from django.utils.translation import ugettext as _

from antxetamedia.tools import admin_image
from antxetamedia.agenda.models import Town, Happening


class TownAdmin(admin.ModelAdmin):
    search_fields = 'name',
admin.site.register(Town)


class HappeningAdmin(admin.ModelAdmin):
    search_fields = 'name', 'organizer', 'description'
    list_display = 'name', 'date', 'time', 'town', 'other_town', 'organizer', 'img'
    img = admin_image('image')
    ordering = '-date',
    fieldsets = (
            (None, {
                'fields': ('name', 'organizer', 'description')}),
            (_('When and where'), {
                'fields': (('date', 'time'), ('town', 'other_town'), 'place')}),
            (_('Details'), {
                'fields': ('image', 'link', 'contact')}),
            )
admin.site.register(Happening, HappeningAdmin)

