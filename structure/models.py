from django.db import models
from django.utils.translation import ugettext as _

from markupfield.fields import MarkupField
from autoslug.fields import AutoSlugField

class NodeManager(models.Manager):
    def roots(self):
        return self.get_query_set().filter(parent__isnull=True)

    def children(self):
        return self.get_query_set().filter(children_set__isnull=True)


class Node(models.Model):
    objects = NodeManager()
    class Meta:
        ordering = 'name',
        verbose_name = _('node')
        verbose_name_plural = _('nodes')

    name = models.CharField(_('name'), max_length=100, unique=True)
    description = MarkupField(_('description'), blank=True, markup_type='plain')

    on_menu = models.BooleanField(_('on menu'), default=False)
    on_frontpage = models.BooleanField(_('on frontpage'), default=False)

    link = models.URLField(_('link'), blank=True)
    image = models.ImageField(_('image'), blank=True, upload_to='img')

    slug = AutoSlugField(editable=False, always_update=True,
            populate_from='name', unique=True)

    parent = models.ForeignKey('self', verbose_name=_('parent'), 
            related_name='children_set', null=True, blank=True, db_index=True)

    def __unicode__(self):
        return self.name

    def descendents(self, including_this=False):
        if including_this:
            yield self

        nodes = [self]
        while nodes:
            node = nodes.pop(0)
            for child in node.children_set.all():
                nodes.append(child)
                yield child

    def ascendents(self, including_this=False):
        if including_this:
            yield self

        node = self
        while parent:
            node = node.parent
            if node:
                yield node
