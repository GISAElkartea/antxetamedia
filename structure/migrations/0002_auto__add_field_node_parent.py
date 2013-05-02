# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Node.parent'
        db.add_column('structure_node', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children_set', null=True, to=orm['structure.Node']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Node.parent'
        db.delete_column('structure_node', 'parent_id')


    models = {
        'structure.node': {
            'Meta': {'object_name': 'Node'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'on_frontpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children_set'", 'null': 'True', 'to': "orm['structure.Node']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['structure']
