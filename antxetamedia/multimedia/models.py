from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from urllib2 import urlopen
from os.path import basename, splitext
from itertools import chain
from operator import attrgetter

from antxetamedia.multimedia.handlers import upload


def get_orphaned_media():
    embeded = EmbededMedia.objects.filter(content_type__isnull=True).iterator()
    medias = Media.objects.filter(content_type__isnull=True).iterator()
    return sorted(chain(embeded, medias), key=attrgetter('pk'), reverse=True)


class EmbededMedia(models.Model):
    class Meta:
        verbose_name = _('embeded media')
        verbose_name_plural = _('embeded medias')

    link = models.URLField(_('link'), max_length=300)
    embed = models.TextField(_('embed code'))

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    related_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.link


class Account(models.Model):
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    name = models.CharField(_('name'), max_length=50)
    user = models.CharField(_('user'), max_length=100, unique=True)
    password = models.CharField(_('password'), max_length=100, blank=True)

    def __unicode__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name = _('media')
        verbose_name_plural = _('medias (audio: MP3 | video: FLV,MP4,H.264)')

    title = models.CharField(_('title'), max_length=300, blank=True)

    account = models.ForeignKey(Account)

    synchronize = models.BooleanField(_('mark for synchronization'), default=True)
    is_synchronized = models.BooleanField(_('synchronization state'),
            default=False)

    remote = models.CharField(max_length=300, editable=False, null=True, blank=True)
    local = models.FileField(_('file'), upload_to='medias', blank=True, null=True,
            max_length=1024, help_text=_('Blank if synchronized'))

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    related_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title

    def clean(self):
        if not (self.is_synchronized or self.local):
            raise ValidationError(_('There must be a file to upload'))

    def get_url(self):
        if self.local:
            return self.local.url
        return self.remote

    def download(self):
        if self.remote:
            temp = NamedTemporaryFile()
            for line in urlopen(self.remote):
                temp.write(line)
            temp.flush()
            self.local.name = basename(self.remote)
            self.local.storage.save(basename(self.remote), File(temp))

    def upload(self):
        uri = upload(fd=self.local.file, **self.get_sync_data())
        if uri:
            self.is_synchronized = True
            self.remote = uri
        else:
            self.is_synchronized = False

    def sync(self):
        self.upload()
        if self.is_synchronized and self.local:
            self.local.delete()

    def get_sync_data(self):
        data = {
                'user': self.account.user,
                'passwd': self.account.password,
                'metadata': settings.S3_METADATA,
                }
        if self.related_object:
            data['bucket'] = self.related_object.slug
            data['metadata'].update(self.related_object.metadata())
        elif self.title:
            data['bucket'] = slugify(self.title)
            data['metadata']['x-archive-meta-title'] = self.title
        else:
            data['bucket'] = 'antxeta'
            data['metadata']['x-archive-meta-title'] = 'Antxeta'
        data['metadata'] = {k: 'uri({})'.format(v) for k, v in data['metadata'].items()}
        data['key'] = '{0}-{1}{2}'.format(
                data['bucket'], self.pk, splitext(self.local.name)[1])
        return data

    def save(self, *args, **kwargs):
        if self.local:
            self.is_synchronized = False
        super(Media, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.local:
            self.local.delete(save=False)
        super(Media, self).delete(*args, **kwargs)
