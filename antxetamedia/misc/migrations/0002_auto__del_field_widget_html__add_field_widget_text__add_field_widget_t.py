# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Widget.html'
        db.delete_column('misc_widget', 'html')

        # Adding field 'Widget.text'
        db.add_column('misc_widget', 'text', self.gf('markupfield.fields.MarkupField')(default='', rendered_field=True), keep_default=False)

        # Adding field 'Widget.text_markup_type'
        db.add_column('misc_widget', 'text_markup_type', self.gf('django.db.models.fields.CharField')(default='', max_length=30), keep_default=False)

        # Adding field 'Widget._text_rendered'
        db.add_column('misc_widget', '_text_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'AboutUs.text_markup_type'
        db.add_column('misc_aboutus', 'text_markup_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=30), keep_default=False)

        # Adding field 'AboutUs._text_rendered'
        db.add_column('misc_aboutus', '_text_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'AboutUs.text'
        db.alter_column('misc_aboutus', 'text', self.gf('markupfield.fields.MarkupField')(rendered_field=True))


    def backwards(self, orm):
        
        # Adding field 'Widget.html'
        db.add_column('misc_widget', 'html', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Deleting field 'Widget.text'
        db.delete_column('misc_widget', 'text')

        # Deleting field 'Widget.text_markup_type'
        db.delete_column('misc_widget', 'text_markup_type')

        # Deleting field 'Widget._text_rendered'
        db.delete_column('misc_widget', '_text_rendered')

        # Deleting field 'AboutUs.text_markup_type'
        db.delete_column('misc_aboutus', 'text_markup_type')

        # Deleting field 'AboutUs._text_rendered'
        db.delete_column('misc_aboutus', '_text_rendered')

        # Changing field 'AboutUs.text'
        db.alter_column('misc_aboutus', 'text', self.gf('django.db.models.fields.TextField')())


    models = {
        'misc.aboutus': {
            'Meta': {'object_name': 'AboutUs'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'})
        },
        'misc.banner': {
            'Meta': {'ordering': "('active', '-id')", 'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'misc.feed': {
            'Meta': {'object_name': 'Feed'},
            'cache': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'how_many': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'where': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'misc.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'misc.widget': {
            'Meta': {'object_name': 'Widget'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'})
        }
    }

    complete_apps = ['misc']
