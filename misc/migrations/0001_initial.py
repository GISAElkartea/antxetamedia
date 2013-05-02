# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Widget'
        db.create_table('misc_widget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('misc', ['Widget'])

        # Adding model 'Link'
        db.create_table('misc_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('misc', ['Link'])

        # Adding model 'Feed'
        db.create_table('misc_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('where', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('how_many', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('cache', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('misc', ['Feed'])

        # Adding model 'Banner'
        db.create_table('misc_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('misc', ['Banner'])

        # Adding model 'AboutUs'
        db.create_table('misc_aboutus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('misc', ['AboutUs'])


    def backwards(self, orm):
        
        # Deleting model 'Widget'
        db.delete_table('misc_widget')

        # Deleting model 'Link'
        db.delete_table('misc_link')

        # Deleting model 'Feed'
        db.delete_table('misc_feed')

        # Deleting model 'Banner'
        db.delete_table('misc_banner')

        # Deleting model 'AboutUs'
        db.delete_table('misc_aboutus')


    models = {
        'misc.aboutus': {
            'Meta': {'object_name': 'AboutUs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
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
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['misc']
