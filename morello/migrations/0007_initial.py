# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table('morello_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address_street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address_city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address_zip', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('morello', ['Organization'])

        # Adding model 'Person'
        db.create_table('morello_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_first', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_middle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_last', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('morello', ['Person'])

        # Adding model 'Client'
        db.create_table('morello_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persons', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['morello.Person'], unique=True)),
            ('race_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('languages_spoken', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('immigration_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('morello', ['Client'])

        # Adding model 'Client_NextDoor'
        db.create_table('morello_client_nextdoor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clients', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['morello.Client'], unique=True)),
            ('why_cx', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('arrested', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('convicted', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('employer_refused', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('employer_declined', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('morello', ['Client_NextDoor'])

        # Adding model 'Notes'
        db.create_table('morello_notes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('morello', ['Notes'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('morello_organization')

        # Deleting model 'Person'
        db.delete_table('morello_person')

        # Deleting model 'Client'
        db.delete_table('morello_client')

        # Deleting model 'Client_NextDoor'
        db.delete_table('morello_client_nextdoor')

        # Deleting model 'Notes'
        db.delete_table('morello_notes')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'morello.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immigration_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'languages_spoken': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'persons': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['morello.Person']", 'unique': 'True'}),
            'race_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'morello.client_nextdoor': {
            'Meta': {'object_name': 'Client_NextDoor'},
            'arrested': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'clients': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['morello.Client']", 'unique': 'True'}),
            'convicted': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'employer_declined': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'employer_refused': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'why_cx': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'morello.notes': {
            'Meta': {'object_name': 'Notes'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'morello.organization': {
            'Meta': {'object_name': 'Organization'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address_zip': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'morello.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_first': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_last': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['morello']