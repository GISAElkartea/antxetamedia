from django.db import models
from django.utils.translation import ugettext as _

from autoslug.fields import AutoSlugField
from markitup.fields import MarkupField


class Project(models.Model):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    name = models.CharField(_('name'), max_length=200)
    image = models.ImageField(_('image'), blank=True, upload_to='img')
    text = MarkupField(_('text'))
    aside = MarkupField(_('aside'), blank=True, null=True)

    slug = AutoSlugField(editable=False, always_update=True, unique=True,
            populate_from='name')

    def __unicode__(self):
        return self.name
