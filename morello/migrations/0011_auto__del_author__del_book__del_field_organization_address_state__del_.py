# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('morello_author')

        # Deleting model 'Book'
        db.delete_table('morello_book')

        # Deleting field 'Organization.address_state'
        db.delete_column('morello_organization', 'address_state')

        # Deleting field 'Client.id'
        db.delete_column('morello_client', 'id')

        # Deleting field 'Client.person'
        db.delete_column('morello_client', 'person_id')

        # Adding field 'Client.person_ptr'
        db.add_column('morello_client', 'person_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['morello.Person'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Author'
        db.create_table('morello_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('morello', ['Author'])

        # Adding model 'Book'
        db.create_table('morello_book', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['morello.Author'])),
        ))
        db.send_create_signal('morello', ['Book'])


        # User chose to not deal with backwards NULL issues for 'Organization.address_state'
        raise RuntimeError("Cannot reverse this migration. 'Organization.address_state' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Client.id'
        raise RuntimeError("Cannot reverse this migration. 'Client.id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Client.person'
        raise RuntimeError("Cannot reverse this migration. 'Client.person' and its values cannot be restored.")
        # Deleting field 'Client.person_ptr'
        db.delete_column('morello_client', 'person_ptr_id')


    models = {
        'morello.client': {
            'Meta': {'object_name': 'Client', '_ormbases': ['morello.Person']},
            'collecting_unemployment': ('django.db.models.fields.SmallIntegerField', [], {}),
            'current_job': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'employment_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'employment_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '5'}),
            'health_insurance': ('django.db.models.fields.SmallIntegerField', [], {}),
            'highest_education': ('django.db.models.fields.SmallIntegerField', [], {}),
            'household_income': ('django.db.models.fields.SmallIntegerField', [], {}),
            'housing_adults': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'housing_children': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'housing_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'housing_situation': ('django.db.models.fields.SmallIntegerField', [], {}),
            'immigration_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'internet_access': ('django.db.models.fields.SmallIntegerField', [], {}),
            'languages_spoken': ('django.db.models.fields.SmallIntegerField', [], {'default': '3'}),
            'marital_status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['morello.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'race_ethnicity': ('django.db.models.fields.SmallIntegerField', [], {}),
            'registered_vote': ('django.db.models.fields.SmallIntegerField', [], {}),
            'unemployment_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'union_job': ('django.db.models.fields.SmallIntegerField', [], {}),
            'why_unemployed': ('django.db.models.fields.SmallIntegerField', [], {'default': '5'})
        },
        'morello.client_nextdoor': {
            'Meta': {'object_name': 'Client_NextDoor'},
            'arrested': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['morello.Client']"}),
            'convicted': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'employer_declined': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'employer_refused': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'why_cx': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'morello.organization': {
            'Meta': {'object_name': 'Organization'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
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