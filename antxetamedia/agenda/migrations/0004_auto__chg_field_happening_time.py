# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Happening.time'
        db.alter_column('agenda_happening', 'time', self.gf('django.db.models.fields.TimeField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Happening.time'
        db.alter_column('agenda_happening', 'time', self.gf('django.db.models.fields.TimeField')(default=None))


    models = {
        'agenda.happening': {
            'Meta': {'ordering': "('date', 'time')", 'object_name': 'Happening'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'contact': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'max_length': '1000', 'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'plain'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'other_town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agenda.Town']", 'null': 'True', 'blank': 'True'})
        },
        'agenda.town': {
            'Meta': {'object_name': 'Town'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['agenda']
