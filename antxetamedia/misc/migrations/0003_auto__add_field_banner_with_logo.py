# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Banner.with_logo'
        db.add_column('misc_banner', 'with_logo', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Banner.with_logo'
        db.delete_column('misc_banner', 'with_logo')


    models = {
        'misc.aboutus': {
            'Meta': {'object_name': 'AboutUs'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'})
        },
        'misc.banner': {
            'Meta': {'ordering': "('active', '-id')", 'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'with_logo': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'misc.feed': {
            'Meta': {'ordering': "('-priority', '-id')", 'object_name': 'Feed'},
            'cache': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'how_many': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'where': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'misc.link': {
            'Meta': {'ordering': "('-priority', '-id')", 'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'misc.widget': {
            'Meta': {'ordering': "('-priority', '-id')", 'object_name': 'Widget'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'})
        }
    }

    complete_apps = ['misc']
