from django.db import models
from django.utils.dates import WEEKDAYS
from django.utils.translation import ugettext as _
from django.conf import settings

from colorful.fields import RGBColorField
from datetime import datetime, date, time, timedelta
from math import ceil

from antxetamedia.structure.models import Node

weekdays = WEEKDAYS.items()

class Colored(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(_('name'), max_length=100)
    color = RGBColorField(_('color'))

    def __unicode__(self):
        return self.name


class Producer(Colored):
    class Meta:
        verbose_name = _('producer')
        verbose_name_plural = _('producers')


class Category(Colored):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Emission(models.Model):
    class Meta:
        verbose_name = _('emission')
        verbose_name_plural = _('emissions')

    name = models.CharField(_('name'), max_length=100)
    producer = models.ForeignKey(Producer)
    category = models.ForeignKey(Category)

    link = models.URLField(_('link'), blank=True)
    program = models.ForeignKey(Node, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Space(models.Model):
    class Meta:
        verbose_name = _('space')
        verbose_name_plural = _('spaces')
        ordering = 'beginning', 'weekday'

    emission = models.ForeignKey(Emission)
    weekday = models.PositiveSmallIntegerField(_('weeday'), choices=weekdays)
    beginning = models.TimeField(_('beginning'))
    ending = models.TimeField(_('ending'))


    def round_up(self, time, minutes):
        time = datetime.combine(date(1, 1, 1), time)
        diff = ceil(time.minute // minutes) * minutes - time.minute
        new = time + timedelta(minutes=diff)
        return new.replace(year=1, month=1, day=1, second=0)

    def rounded_beginning(self):
        return self.round_up(self.beginning, settings.PROGRAMMING_SPACE)

    def rounded_ending(self):
        return self.round_up(self.ending, settings.PROGRAMMING_SPACE)

    def get_pieces(self):
        current = self.rounded_beginning()
        while current.time() != self.rounded_ending().time():
            yield current.time()
            current += timedelta(minutes=settings.PROGRAMMING_SPACE)

    def get_first(self):
        return self.rounded_beginning().time()

    def get_last(self):
        return (self.rounded_ending() - timedelta(minutes=settings.PROGRAMMING_SPACE)).time()

    def has_yesterday(self):
        return Space.objects.filter(
                emission=self.emission, weekday=(self.weekday - 1),
                beginning=self.beginning, ending=self.ending,).count()

    def has_tomorrow(self):
        return Space.objects.filter(
                emission=self.emission, weekday=(self.weekday + 1),
                beginning=self.beginning, ending=self.ending,).count()
