from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import ugettext as _

from markupfield.fields import MarkupField
from urllib2 import urlopen
from feedparser import parse
from pickle import dumps, loads

HEADLINE = 0
PANEL = 1

class Misc(models.Model):
    class Meta:
        abstract = True

    priorities = (
            (0, _('Low')),
            (1, _('Medium')),
            (2, _('High')),
            )

    name = models.CharField(_('name'), max_length=100)
    priority = models.PositiveSmallIntegerField(_('priority'), choices=priorities)

    def __unicode__(self):
        return self.name


class Widget(Misc):
    class Meta:
        ordering = '-priority', '-id'
        verbose_name = _('widget')
        verbose_name_plural = _('widgets')

    text = MarkupField(_('text'))


class Link(Misc):
    class Meta:
        ordering = '-priority', '-id'
        verbose_name = _('link')
        verbose_name_plural = _('links')

    link = models.URLField(_('link'))


class Feed(Misc):
    class Meta:
        ordering = '-priority', '-id'
        verbose_name = _('feed')
        verbose_name_plural = _('feeds')

    types = (
            (HEADLINE, _('Headline')),
            (PANEL, _('Panel')),
            )

    url = models.URLField(_('url'), help_text=_('URL of the RSS'))
    where = models.PositiveSmallIntegerField(_('where'), choices=types,
            help_text=_('Where is the feed shown?'))
    how_many = models.PositiveSmallIntegerField(_('how many'), default=5,
            help_text=_('How many feeds must we have?'))

    cache = models.TextField(editable=False, blank=True)

    def update(self):
        feed = urlopen(self.url)
        feed = parse(feed)

        posts = []
        for post in feed['entries'][:self.how_many]:
            posts.append({
                'title': strip_tags(post.title),
                'link': post.link,
                })
        self.cache = dumps(posts).encode('base64')
        self.save()

    def posts(self):
        if self.cache:
            return loads(self.cache.decode('base64'))
        return ''


class Banner(models.Model):
    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')
        ordering = '-active', '-id'

    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(_('image'), upload_to='img')
    active = models.BooleanField(_('active'), default=False)
    with_logo = models.BooleanField(_('with logo'), default=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            try:
                old = Banner.objects.get(active=True)
            except Banner.DoesNotExist:
                pass
            else:
                if old.pk is not self.pk:
                    old.active = False
                    old.save()
        super(Banner, self).save(*args, **kwargs)


class AboutUs(models.Model):
    class Meta:
        verbose_name = _('about us')
        verbose_name_plural = _('about us')

    text = MarkupField(_('text'), default_markup_type='markdown')

    def __unicode__(self):
        return _('about us')
