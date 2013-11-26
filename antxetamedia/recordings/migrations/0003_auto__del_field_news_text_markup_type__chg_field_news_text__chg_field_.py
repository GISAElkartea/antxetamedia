# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'News.text_markup_type'
        db.delete_column(u'recordings_news', 'text_markup_type')


        # Changing field 'News.text'
        db.alter_column(u'recordings_news', 'text', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))

        # Changing field 'News.slug'
        db.alter_column(u'recordings_news', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=()))
        # Deleting field 'Program.text_markup_type'
        db.delete_column(u'recordings_program', 'text_markup_type')


        # Changing field 'Program.text'
        db.alter_column(u'recordings_program', 'text', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))

        # Changing field 'NewsCategory.slug'
        db.alter_column(u'recordings_newscategory', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=()))

    def backwards(self, orm):
        # Adding field 'News.text_markup_type'
        db.add_column(u'recordings_news', 'text_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='plain', max_length=30),
                      keep_default=False)


        # Changing field 'News.text'
        db.alter_column(u'recordings_news', 'text', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'News.slug'
        db.alter_column(u'recordings_news', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), unique=True, populate_from=None))
        # Adding field 'Program.text_markup_type'
        db.add_column(u'recordings_program', 'text_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='plain', max_length=30),
                      keep_default=False)


        # Changing field 'Program.text'
        db.alter_column(u'recordings_program', 'text', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'NewsCategory.slug'
        db.alter_column(u'recordings_newscategory', 'slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), unique=True, populate_from=None))

    models = {
        u'recordings.news': {
            'Meta': {'ordering': "('-principal', '-pub_date', '-id')", 'object_name': 'News'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['recordings.NewsCategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 26, 0, 0)'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'text': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'recordings.newscategory': {
            'Meta': {'object_name': 'NewsCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'recordings.program': {
            'Meta': {'ordering': "('-principal', '-pub_date', '-id')", 'object_name': 'Program'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['structure.Node']"}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 26, 0, 0)'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'text': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
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

    complete_apps = ['recordings']