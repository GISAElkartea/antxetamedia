# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.beginning'
        db.add_column(u'projects_project', 'beginning',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today),
                      keep_default=False)


        # Changing field 'Project.aside'
        db.alter_column(u'projects_project', 'aside', self.gf('markitup.fields.MarkupField')(null=True, no_rendered_field=True))

    def backwards(self, orm):
        # Deleting field 'Project.beginning'
        db.delete_column(u'projects_project', 'beginning')


        # Changing field 'Project.aside'
        db.alter_column(u'projects_project', 'aside', self.gf('markitup.fields.MarkupField')(default='', no_rendered_field=True))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'multimedia.account': {
            'Meta': {'object_name': 'Account'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'multimedia.embededmedia': {
            'Meta': {'object_name': 'EmbededMedia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'embed': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'})
        },
        u'multimedia.media': {
            'Meta': {'object_name': 'Media'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multimedia.Account']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_synchronized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'remote': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'synchronize': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            '_aside_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'aside': ('markitup.fields.MarkupField', [], {'default': "''", 'null': 'True', 'blank': 'True', 'no_rendered_field': 'True'}),
            'beginning': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'text': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True'})
        }
    }

    complete_apps = ['projects']