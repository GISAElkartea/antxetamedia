# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Category.color'
        db.add_column('programming_category', 'color', self.gf('colorful.fields.RGBColorField')(default='', max_length=7), keep_default=False)

        # Adding field 'Producer.color'
        db.add_column('programming_producer', 'color', self.gf('colorful.fields.RGBColorField')(default='', max_length=7), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Category.color'
        db.delete_column('programming_category', 'color')

        # Deleting field 'Producer.color'
        db.delete_column('programming_producer', 'color')


    models = {
        'programming.category': {
            'Meta': {'object_name': 'Category'},
            'color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programming.emission': {
            'Meta': {'object_name': 'Emission'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Producer']"}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['structure.Node']", 'null': 'True', 'blank': 'True'})
        },
        'programming.producer': {
            'Meta': {'object_name': 'Producer'},
            'color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programming.space': {
            'Meta': {'ordering': "('beginning', 'weekday')", 'object_name': 'Space'},
            'beginning': ('django.db.models.fields.TimeField', [], {}),
            'emission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Emission']"}),
            'ending': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weekday': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'structure.node': {
            'Meta': {'object_name': 'Node'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'on_frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_set'", 'null': 'True', 'to': "orm['structure.Node']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['programming']
