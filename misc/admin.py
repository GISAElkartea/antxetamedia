from django.contrib import admin

from misc.models import Widget, Feed, Link, Banner, AboutUs

from tools import admin_color, admin_image


class MiscAdmin(admin.ModelAdmin):
    colors = {
            0: 'green',
            1: 'blue',
            2: 'red',
            }
    prio = admin_color('priority', 'colors')


class WidgetAdmin(MiscAdmin):
    list_display = 'name', 'priority'
    fieldsets = (
            (None, {
                'fields': (('name', 'priority'), 'text_markup_type', 'text')}),
            )
admin.site.register(Widget, WidgetAdmin)


class LinkAdmin(MiscAdmin):
    list_display = 'name', 'link', 'priority'
    fieldsets = (
            (None, {
                'fields': (('name', 'priority'), 'link')}),
            )
admin.site.register(Link, LinkAdmin)


class FeedAdmin(MiscAdmin):
    list_display = 'name', 'url', 'where', 'how_many', 'priority'
    fieldsets = (
            (None, {
                'fields': (('name', 'priority'), 'url', ('where', 'how_many'))}),
            )
admin.site.register(Feed, FeedAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = 'name', 'active', 'with_logo', 'img'
    img = admin_image('image')
    fieldsets = (
            (None, {
                'fields': (('name', 'active', 'with_logo'), 'image')}),
            )
admin.site.register(Banner, BannerAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = '__unicode__',
    fields = 'text_markup_type', 'text',
admin.site.register(AboutUs, AboutUsAdmin)
