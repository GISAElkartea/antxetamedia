# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.aside'
        db.add_column(u'projects_project', 'aside',
                      self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True, blank=True),
                      keep_default=False)

        # Adding field 'Project._aside_rendered'
        db.add_column(u'projects_project', '_aside_rendered',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.aside'
        db.delete_column(u'projects_project', 'aside')

        # Deleting field 'Project._aside_rendered'
        db.delete_column(u'projects_project', '_aside_rendered')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            '_aside_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'aside': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'text': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True'})
        }
    }

    complete_apps = ['projects']