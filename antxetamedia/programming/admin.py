from django.contrib import admin
from django.utils.translation import ugettext as _

from antxetamedia.programming.models import Producer, Category, Emission, Space


class SpaceAdmin(admin.TabularInline):
    model = Space
    extra = 0


class EmissionAdmin(admin.ModelAdmin):
    list_display = 'name', 'producer', 'category', 'program'
    inlines = SpaceAdmin,
    fieldsets = (
            (None, {
                'fields': ('name', 'producer', 'category')}),
            (_('Details'), {
                'fields': ('program', 'link')}),
            )
admin.site.register(Emission, EmissionAdmin)


class ColoredAdmin(admin.ModelAdmin):
    list_display = 'name', 'html_color'

    def html_color(self, obj):
        return u'<div style="background: %s;">&nbsp;</div>' % obj.color
    html_color.short_description = _('color')
    html_color.allow_tags = True
admin.site.register(Producer, ColoredAdmin)
admin.site.register(Category, ColoredAdmin)
