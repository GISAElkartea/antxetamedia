# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Node.description_markup_type'
        db.add_column('structure_node', 'description_markup_type', self.gf('django.db.models.fields.CharField')(default='plain', max_length=30, blank=True), keep_default=False)

        # Adding field 'Node._description_rendered'
        db.add_column('structure_node', '_description_rendered', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Changing field 'Node.description'
        db.alter_column('structure_node', 'description', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Adding unique constraint on 'Node', fields ['name']
        db.create_unique('structure_node', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Node', fields ['name']
        db.delete_unique('structure_node', ['name'])

        # Deleting field 'Node.description_markup_type'
        db.delete_column('structure_node', 'description_markup_type')

        # Deleting field 'Node._description_rendered'
        db.delete_column('structure_node', '_description_rendered')

        # Changing field 'Node.description'
        db.alter_column('structure_node', 'description', self.gf('django.db.models.fields.TextField')())


    models = {
        'structure.node': {
            'Meta': {'object_name': 'Node'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True', 'blank': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'plain'", 'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'on_frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_set'", 'null': 'True', 'to': "orm['structure.Node']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['structure']
