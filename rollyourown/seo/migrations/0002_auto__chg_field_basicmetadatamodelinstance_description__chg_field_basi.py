# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BasicMetadataModelInstance.description'
        db.alter_column(u'seo_basicmetadatamodelinstance', 'description', self.gf('django.db.models.fields.CharField')(max_length=305))

        # Changing field 'BasicMetadataModel.description'
        db.alter_column(u'seo_basicmetadatamodel', 'description', self.gf('django.db.models.fields.CharField')(max_length=305))

        # Changing field 'BasicMetadataPath.description'
        db.alter_column(u'seo_basicmetadatapath', 'description', self.gf('django.db.models.fields.CharField')(max_length=305))

        # Changing field 'BasicMetadataView.description'
        db.alter_column(u'seo_basicmetadataview', 'description', self.gf('django.db.models.fields.CharField')(max_length=305))

    def backwards(self, orm):

        # Changing field 'BasicMetadataModelInstance.description'
        db.alter_column(u'seo_basicmetadatamodelinstance', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'BasicMetadataModel.description'
        db.alter_column(u'seo_basicmetadatamodel', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'BasicMetadataPath.description'
        db.alter_column(u'seo_basicmetadatapath', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'BasicMetadataView.description'
        db.alter_column(u'seo_basicmetadataview', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

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
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '305', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '305', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '305', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '305', 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'og_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '511', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['seo']