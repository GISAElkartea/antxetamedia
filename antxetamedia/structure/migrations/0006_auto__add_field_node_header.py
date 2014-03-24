# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Node.header'
        db.add_column(u'structure_node', 'header',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Node.header'
        db.delete_column(u'structure_node', 'header')


    models = {
        u'structure.node': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Node'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_panel_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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