from datetime import date

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from django.utils.six import text_type

from autoslug.fields import AutoSlugField
from markitup.fields import MarkupField

from antxetamedia.multimedia.models import Media, EmbededMedia


class Project(models.Model):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    name = models.CharField(_('name'), max_length=200)
    image = models.ImageField(_('image'), blank=True, upload_to='img')
    text = MarkupField(_('text'))
    aside = MarkupField(_('aside'), blank=True, null=True, default='')
    beginning = models.DateField(default=date.today,
                                 verbose_name=_('beginning date'))

    medias = generic.GenericRelation(Media)
    embeded_medias = generic.GenericRelation(EmbededMedia)

    slug = AutoSlugField(editable=False, always_update=True, unique=True,
            populate_from='name')

    def __unicode__(self):
        return self.name

    def metadata(self):
        return {
                'x-archive-meta-title': text_type(self),
                'x-archive-meta-creator': text_type('Antxeta Irratia'),
                'x-archive-meta-description': text_type(self.text.raw),
                'x-archive-meta-subject': text_type(self),
                'x-archive-meta-date': self.beginning.strftime('%Y-%m-%d'),
                }
