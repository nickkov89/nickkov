# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table('dormroof_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('importance_level', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
        ))
        db.send_create_signal('dormroof', ['Message'])

        # Adding model 'Event'
        db.create_table('dormroof_event', (
            ('message_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dormroof.Message'], unique=True, primary_key=True)),
            ('where', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('when', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('dormroof', ['Event'])

        # Adding model 'University'
        db.create_table('dormroof_university', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dormroof', ['University'])

        # Adding model 'Community'
        db.create_table('dormroof_community', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.University'])),
        ))
        db.send_create_signal('dormroof', ['Community'])

        # Adding model 'Building'
        db.create_table('dormroof_building', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('community', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.Community'])),
        ))
        db.send_create_signal('dormroof', ['Building'])

        # Adding model 'UserProfile'
        db.create_table('dormroof_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('accepted_eula', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.Building'])),
            ('community', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.Community'])),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_ra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('belongs_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.UserProfile'], null=True)),
            ('is_rd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('favorite_movies', self.gf('django.db.models.fields.TextField')()),
            ('favorite_books', self.gf('django.db.models.fields.TextField')()),
            ('favorite_music', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dormroof', ['UserProfile'])

        # Adding model 'Infraction'
        db.create_table('dormroof_infraction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('dormroof', ['Infraction'])

        # Adding model 'Infraction_Meta'
        db.create_table('dormroof_infraction_meta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.Infraction'])),
            ('when', self.gf('django.db.models.fields.DateField')()),
            ('given_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dormroof.UserProfile'])),
            ('given_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='infracted_user', to=orm['dormroof.UserProfile'])),
        ))
        db.send_create_signal('dormroof', ['Infraction_Meta'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('dormroof_message')

        # Deleting model 'Event'
        db.delete_table('dormroof_event')

        # Deleting model 'University'
        db.delete_table('dormroof_university')

        # Deleting model 'Community'
        db.delete_table('dormroof_community')

        # Deleting model 'Building'
        db.delete_table('dormroof_building')

        # Deleting model 'UserProfile'
        db.delete_table('dormroof_userprofile')

        # Deleting model 'Infraction'
        db.delete_table('dormroof_infraction')

        # Deleting model 'Infraction_Meta'
        db.delete_table('dormroof_infraction_meta')


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
        'dormroof.building': {
            'Meta': {'object_name': 'Building'},
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.Community']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'dormroof.community': {
            'Meta': {'object_name': 'Community'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.University']"})
        },
        'dormroof.event': {
            'Meta': {'object_name': 'Event', '_ormbases': ['dormroof.Message']},
            'message_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dormroof.Message']", 'unique': 'True', 'primary_key': 'True'}),
            'when': ('django.db.models.fields.DateField', [], {}),
            'where': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'dormroof.infraction': {
            'Meta': {'object_name': 'Infraction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'dormroof.infraction_meta': {
            'Meta': {'object_name': 'Infraction_Meta'},
            'given_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.UserProfile']"}),
            'given_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'infracted_user'", 'to': "orm['dormroof.UserProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.Infraction']"}),
            'when': ('django.db.models.fields.DateField', [], {})
        },
        'dormroof.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance_level': ('django.db.models.fields.IntegerField', [], {}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'dormroof.university': {
            'Meta': {'object_name': 'University'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dormroof.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'accepted_eula': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'belongs_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.UserProfile']", 'null': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.Building']"}),
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dormroof.Community']"}),
            'favorite_books': ('django.db.models.fields.TextField', [], {}),
            'favorite_movies': ('django.db.models.fields.TextField', [], {}),
            'favorite_music': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_ra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_rd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dormroof']