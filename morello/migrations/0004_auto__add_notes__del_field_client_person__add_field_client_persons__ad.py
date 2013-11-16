# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Notes'
        db.create_table('morello_notes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('morello', ['Notes'])

        # Deleting field 'Client.person'
        db.delete_column('morello_client', 'person_id')

        # Adding field 'Client.persons'
        db.add_column('morello_client', 'persons',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['morello.Person'], unique=True),
                      keep_default=False)

        # Adding field 'Client.race_ethnicity'
        db.add_column('morello_client', 'race_ethnicity',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client.languages_spoken'
        db.add_column('morello_client', 'languages_spoken',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client.marital_status'
        db.add_column('morello_client', 'marital_status',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client_NextDoor.clients'
        db.add_column('morello_client_nextdoor', 'clients',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['morello.Client'], unique=True),
                      keep_default=False)

        # Adding field 'Client_NextDoor.arrested'
        db.add_column('morello_client_nextdoor', 'arrested',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client_NextDoor.convicted'
        db.add_column('morello_client_nextdoor', 'convicted',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client_NextDoor.employer_refused'
        db.add_column('morello_client_nextdoor', 'employer_refused',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)

        # Adding field 'Client_NextDoor.employer_declined'
        db.add_column('morello_client_nextdoor', 'employer_declined',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Notes'
        db.delete_table('morello_notes')


        # User chose to not deal with backwards NULL issues for 'Client.person'
        raise RuntimeError("Cannot reverse this migration. 'Client.person' and its values cannot be restored.")
        # Deleting field 'Client.persons'
        db.delete_column('morello_client', 'persons_id')

        # Deleting field 'Client.race_ethnicity'
        db.delete_column('morello_client', 'race_ethnicity')

        # Deleting field 'Client.languages_spoken'
        db.delete_column('morello_client', 'languages_spoken')

        # Deleting field 'Client.marital_status'
        db.delete_column('morello_client', 'marital_status')

        # Deleting field 'Client_NextDoor.clients'
        db.delete_column('morello_client_nextdoor', 'clients_id')

        # Deleting field 'Client_NextDoor.arrested'
        db.delete_column('morello_client_nextdoor', 'arrested')

        # Deleting field 'Client_NextDoor.convicted'
        db.delete_column('morello_client_nextdoor', 'convicted')

        # Deleting field 'Client_NextDoor.employer_refused'
        db.delete_column('morello_client_nextdoor', 'employer_refused')

        # Deleting field 'Client_NextDoor.employer_declined'
        db.delete_column('morello_client_nextdoor', 'employer_declined')


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