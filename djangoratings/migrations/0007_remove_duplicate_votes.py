# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from djangoratings.models import Vote


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Delete duplicates
        votes = Vote.objects.all()
        for vote in votes:
            if Vote.objects.filter(content_type=vote.content_type, 
                                   object_id=vote.object_id, 
                                   key=vote.key, 
                                   user=vote.user, 
                                   ip_address=vote.ip_address).count() > 1:
                vote.delete()


    def backwards(self, orm):
        pass

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'djangoratings.ignoredobject': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'IgnoredObject'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'djangoratings.score': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'key'),)", 'object_name': 'Score'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'djangoratings.similaruser': {
            'Meta': {'unique_together': "(('from_user', 'to_user'),)", 'object_name': 'SimilarUser'},
            'agrees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'disagrees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'exclude': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'similar_users'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'similar_users_from'", 'to': u"orm['auth.User']"})
        },
        u'djangoratings.vote': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'key', 'user', 'ip_address', 'cookie'),)", 'object_name': 'Vote'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': u"orm['contenttypes.ContentType']"}),
            'cookie': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'votes'", 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['djangoratings']
