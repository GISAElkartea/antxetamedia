from django.contrib import admin
from django.utils.translation import ugettext as _

from tools import admin_image
from recordings.models import News, NewsCategory, Program
from multimedia.admin import MediaInline, EmbededMediaInline,\
        MediaRelated


class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = 'name',
admin.site.register(NewsCategory, NewsCategoryAdmin)


class RecordAdmin(MediaRelated):
    ordering = '-pub_date',
    date_hierarchy = 'pub_date'
    actions = 'mark_for_synchronization',
    inlines = MediaInline, EmbededMediaInline
    img = admin_image('image')
    list_per_page = 50


class NewsAdmin(RecordAdmin):
    list_display = 'title', 'pub_date', 'principal', 'img'
    list_filter = 'categories', 'pub_date',
    search_fields = 'title', 'text'
    fieldsets = (
            (None, {
                'fields': (('title', 'principal'), 'text')}),
            (_('Details'), {
                'fields': ('categories', 'tags', 'image', 'link', 'pub_date')}),
            )
admin.site.register(News, NewsAdmin)


class ProgramAdmin(RecordAdmin):
    list_display = '__unicode__', 'type', 'program', 'pub_date', 'principal', 'img'
    list_filter = 'type', 'program', 'pub_date'
    list_editable = 'type', 'program'
    search_fields = 'text',
    fieldsets = (
            (None, {
                'fields': (('title', 'principal'), 'type', 'text')}),
            (_('Details'), {
                'fields': ('program', 'tags', 'image', 'link', 'pub_date')}),
            )
admin.site.register(Program, ProgramAdmin)
