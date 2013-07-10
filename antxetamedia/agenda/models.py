from django.db import models
from django.utils.translation import ugettext as _

from datetime import date
from markupfield.fields import MarkupField
from autoslug.fields import AutoSlugField


class Town(models.Model):
    class Meta:
        verbose_name = _('town')
        verbose_name_plural = _('towns')

    name = models.CharField(_('name'), max_length=100, unique=True)

    slug = AutoSlugField(editable=False, always_update=True, unique=True,
            populate_from='name')
    
    def __unicode__(self):
        return self.name


class HappeningManager(models.Manager):
    def future(self):
        return self.get_query_set().filter(
                date__gte=date.today())


class Happening(models.Model):
    objects = HappeningManager()
    class Meta:
        verbose_name = _('Happening')
        verbose_name_plural = _('Happenings')
        ordering = 'date', 'time'

    name = models.CharField(_('name'), max_length=150)
    organizer = models.CharField(_('organizer'), max_length=50, blank=True)
    description = MarkupField(_('description'), max_length=1000,
            markup_type='plain', escape_html=True)

    date = models.DateField(_('date'))
    time = models.TimeField(_('time'), null=True, blank=True)

    town = models.ForeignKey(Town, blank=True, null=True)
    other_town = models.CharField(_('other'), max_length=100, blank=True)
    place = models.CharField(_('place'), max_length=300, blank=True)

    image = models.ImageField(_('image'), blank=True, upload_to='img')
    link = models.URLField(_('link'), blank=True)
    contact = models.EmailField(_('contact'), blank=True)

    slug = AutoSlugField(editable=False, always_update=True, unique=True,
            populate_from='name')

    def __unicode__(self):
        return self.name

    def get_town(self):
        if self.town:
            return self.town
        return self.other_town

    @models.permalink
    def get_absolute_url(self):
        return 'agenda:detail', (), {'slug': self.slug}
