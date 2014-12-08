# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BasicMetadataPath'
        db.create_table(u'seo_basicmetadatapath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('_path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'seo', ['BasicMetadataPath'])

        # Adding unique constraint on 'BasicMetadataPath', fields ['_path']
        db.create_unique(u'seo_basicmetadatapath', ['_path'])

        # Adding model 'BasicMetadataModelInstance'
        db.create_table(u'seo_basicmetadatamodelinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('_path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('_content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'seo', ['BasicMetadataModelInstance'])

        # Adding unique constraint on 'BasicMetadataModelInstance', fields ['_path']
        db.create_unique(u'seo_basicmetadatamodelinstance', ['_path'])

        # Adding unique constraint on 'BasicMetadataModelInstance', fields ['_content_type', '_object_id']
        db.create_unique(u'seo_basicmetadatamodelinstance', ['_content_type_id', '_object_id'])

        # Adding model 'BasicMetadataModel'
        db.create_table(u'seo_basicmetadatamodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('_content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal(u'seo', ['BasicMetadataModel'])

        # Adding unique constraint on 'BasicMetadataModel', fields ['_content_type']
        db.create_unique(u'seo_basicmetadatamodel', ['_content_type_id'])

        # Adding model 'BasicMetadataView'
        db.create_table(u'seo_basicmetadataview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_title', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('og_description', self.gf('django.db.models.fields.CharField')(default='', max_length=511, blank=True)),
            ('_view', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255, blank=True)),
        ))
        db.send_create_signal(u'seo', ['BasicMetadataView'])

        # Adding unique constraint on 'BasicMetadataView', fields ['_view']
        db.create_unique(u'seo_basicmetadataview', ['_view'])


    def backwards(self, orm):
        # Removing unique constraint on 'BasicMetadataView', fields ['_view']
        db.delete_unique(u'seo_basicmetadataview', ['_view'])

        # Removing unique constraint on 'BasicMetadataModel', fields ['_content_type']
        db.delete_unique(u'seo_basicmetadatamodel', ['_content_type_id'])

        # Removing unique constraint on 'BasicMetadataModelInstance', fields ['_content_type', '_object_id']
        db.delete_unique(u'seo_basicmetadatamodelinstance', ['_content_type_id', '_object_id'])

        # Removing unique constraint on 'BasicMetadataModelInstance', fields ['_path']
        db.delete_unique(u'seo_basicmetadatamodelinstance', ['_path'])

        # Removing unique constraint on 'BasicMetadataPath', fields ['_path']
        db.delete_unique(u'seo_basicmetadatapath', ['_path'])

        # Deleting model 'BasicMetadataPath'
        db.delete_table(u'seo_basicmetadatapath')

        # Deleting model 'BasicMetadataModelInstance'
        db.delete_table(u'seo_basicmetadatamodelinstance')

        # Deleting model 'BasicMetadataModel'
        db.delete_table(u'seo_basicmetadatamodel')

        # Deleting model 'BasicMetadataView'
        db.delete_table(u'seo_basicmetadataview')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'seo.basicmetadatamodel': {
            'Meta': {'unique_together': "(('_content_type',),)", 'object_name': 'BasicMetadataModel'},
            '_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'seo.basicmetadatamodelinstance': {
            'Meta': {'unique_together': "(('_path',), ('_content_type', '_object_id'))", 'object_name': 'BasicMetadataModelInstance'},
            '_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            '_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            '_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'seo.basicmetadatapath': {
            'Meta': {'unique_together': "(('_path',),)", 'object_name': 'BasicMetadataPath'},
            '_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'seo.basicmetadataview': {
            'Meta': {'unique_together': "(('_view',),)", 'object_name': 'BasicMetadataView'},
            '_view': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['seo']