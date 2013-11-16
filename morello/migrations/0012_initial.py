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
            ('address_state', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('address_zip', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('morello', ['Organization'])

        # Adding model 'Person'
        db.create_table('morello_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_first', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_middle', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('name_last', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('morello', ['Person'])

        # Adding model 'Client'
        db.create_table('morello_client', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['morello.Person'], unique=True, primary_key=True)),
            ('race_ethnicity', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('languages_spoken', self.gf('django.db.models.fields.SmallIntegerField')(default=3, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('immigration_status', self.gf('django.db.models.fields.SmallIntegerField')(default=2, blank=True)),
            ('highest_education', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('registered_vote', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('internet_access', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('health_insurance', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('employment_status', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('current_job', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('employment_period', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2, blank=True)),
            ('union_job', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('why_unemployed', self.gf('django.db.models.fields.SmallIntegerField')(default=5, blank=True)),
            ('unemployment_period', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2, blank=True)),
            ('collecting_unemployment', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('housing_situation', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('housing_adults', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2, blank=True)),
            ('housing_children', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2, blank=True)),
            ('housing_period', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2, blank=True)),
            ('household_income', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('morello', ['Client'])

        # Adding model 'Client_NextDoor'
        db.create_table('morello_client_nextdoor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['morello.Client'])),
            ('why_cx', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('arrested', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('convicted', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('employer_refused', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('employer_declined', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('morello', ['Client_NextDoor'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('morello_organization')

        # Deleting model 'Person'
        db.delete_table('morello_person')

        # Deleting model 'Client'
        db.delete_table('morello_client')

        # Deleting model 'Client_NextDoor'
        db.delete_table('morello_client_nextdoor')


    models = {
        'morello.client': {
            'Meta': {'object_name': 'Client', '_ormbases': ['morello.Person']},
            'collecting_unemployment': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'current_job': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'employment_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'employment_status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'health_insurance': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'highest_education': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'household_income': ('django.db.models.fields.SmallIntegerField', [], {}),
            'housing_adults': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'housing_children': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'housing_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'housing_situation': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'immigration_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2', 'blank': 'True'}),
            'internet_access': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'languages_spoken': ('django.db.models.fields.SmallIntegerField', [], {'default': '3', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['morello.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'race_ethnicity': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'registered_vote': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'unemployment_period': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'union_job': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'why_unemployed': ('django.db.models.fields.SmallIntegerField', [], {'default': '5', 'blank': 'True'})
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
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
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
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['morello']