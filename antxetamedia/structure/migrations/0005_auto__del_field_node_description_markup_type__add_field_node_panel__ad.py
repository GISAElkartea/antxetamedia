# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Node.description_markup_type'
        db.delete_column(u'structure_node', 'description_markup_type')

        # Adding field 'Node.panel'
        db.add_column(u'structure_node', 'panel',
                      self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True, blank=True),
                      keep_default=True)

        # Adding field 'Node._panel_rendered'
        db.add_column(u'structure_node', '_panel_rendered',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=True)


        # Changing field 'Node.description'
        db.alter_column(u'structure_node', 'description', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))

        # Changing field 'Node.slug'
        db.alter_column(u'structure_node', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=()))

    def backwards(self, orm):
        # Adding field 'Node.description_markup_type'
        db.add_column(u'structure_node', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='plain', max_length=30, blank=True),
                      keep_default=True)

        # Deleting field 'Node.panel'
        db.delete_column(u'structure_node', 'panel')

        # Deleting field 'Node._panel_rendered'
        db.delete_column(u'structure_node', '_panel_rendered')


        # Changing field 'Node.description'
        db.alter_column(u'structure_node', 'description', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'Node.slug'
        db.alter_column(u'structure_node', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), unique=True, populate_from=None))

    models = {
        u'structure.node': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Node'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_panel_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'on_frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'panel': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_set'", 'null': 'True', 'to': u"orm['structure.Node']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        }
    }

    complete_apps = ['structure']
