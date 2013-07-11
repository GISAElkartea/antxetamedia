from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.utils.translation import ugettext as _

from antxetamedia.multimedia.models import Account, Media, EmbededMedia
from antxetamedia.multimedia.forms import AccountForm

class AccountAdmin(admin.ModelAdmin):
    form = AccountForm
admin.site.register(Account, AccountAdmin)


class EmbededMediaAdmin(admin.ModelAdmin):
    readonly_fields = 'content_type', 'object_id'
    fieldsets = (
            (None, {
                'fields': ('link', 'embed')}),
            (_('Related'), {
                'fields': ('content_type', 'object_id')}),
            )
admin.site.register(EmbededMedia, EmbededMediaAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = '__unicode__', 'account', 'synchronize', 'is_synchronized',
    list_filter = 'synchronize', 'is_synchronized'
    readonly_fields = 'is_synchronized', 'content_type', 'object_id'
    fieldsets = (
            (None, {
                'fields': ('title', ('synchronize', 'is_synchronized'), 
                    ('account', 'local'))}),
            (_('Related'), {
                'fields': ('content_type', 'object_id')}),
            )
admin.site.register(Media, MediaAdmin)


class EmbededMediaInline(generic.GenericTabularInline):
    model = EmbededMedia
    extra = 0
    fields = 'link', 'embed'


class MediaInline(generic.GenericTabularInline):
    model = Media
    extra = 0
    fields = 'title', 'account', 'local', 'synchronize', 'is_synchronized'
    readonly_fields = 'is_synchronized',


class MediaRelated(admin.ModelAdmin):
    def get_media_for_obj(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        return Media.objects.filter(
                content_type__pk=content_type.pk,
                object_id=obj.id)


    def get_media_for_queryset(self, queryset):
        content_type = ContentType.objects.get_for_model(queryset.model)
        object_pks = ( pk[0] for pk in queryset.values_list('pk').iterator() )
        return Media.objects.filter(
                content_type__pk=content_type.pk,
                object_id__in=object_pks)


    def synchronized(self, obj):
        return self.get_media_for_obj(obj).filter(
                is_synchronized=False).count() is 0
    synchronized.boolean = True
    synchronized.short_description = _('Synchronized')


    def save_model(self, request, obj, form, change):
        if change:
            medias = self.get_media_for_obj(obj)
            for media in medias:
                media.is_synchronized = False
                media.save()
        obj.save()


    def mark_for_synchronization(self, request, queryset):
        not_marked = self.get_media_for_queryset(queryset).filter(
                synchronize=False)

        for media in not_marked:
            media.synchronize = True
            media.save()
    mark_for_synchronization.short_description = _('Mark for synchronization')
