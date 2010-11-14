# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Country.last_modified'
        db.delete_column('guides_country', 'last_modified')

        # Deleting field 'Country.pub_date'
        db.delete_column('guides_country', 'pub_date')

        # Adding field 'Country.created'
        db.add_column('guides_country', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Adding field 'Country.modified'
        db.add_column('guides_country', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Deleting field 'Guide.last_modified'
        db.delete_column('guides_guide', 'last_modified')

        # Deleting field 'Guide.pub_date'
        db.delete_column('guides_guide', 'pub_date')

        # Adding field 'Guide.start_date'
        db.add_column('guides_guide', 'start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Guide.end_date'
        db.add_column('guides_guide', 'end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Guide.created'
        db.add_column('guides_guide', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Adding field 'Guide.modified'
        db.add_column('guides_guide', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Deleting field 'City.last_modified'
        db.delete_column('guides_city', 'last_modified')

        # Deleting field 'City.pub_date'
        db.delete_column('guides_city', 'pub_date')

        # Adding field 'City.created'
        db.add_column('guides_city', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Adding field 'City.modified'
        db.add_column('guides_city', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Deleting field 'Region.last_modified'
        db.delete_column('guides_region', 'last_modified')

        # Deleting field 'Region.pub_date'
        db.delete_column('guides_region', 'pub_date')

        # Adding field 'Region.created'
        db.add_column('guides_region', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Adding field 'Region.modified'
        db.add_column('guides_region', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Deleting field 'Spot.last_modified'
        db.delete_column('guides_spot', 'last_modified')

        # Deleting field 'Spot.pub_date'
        db.delete_column('guides_spot', 'pub_date')

        # Adding field 'Spot.created'
        db.add_column('guides_spot', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)

        # Adding field 'Spot.modified'
        db.add_column('guides_spot', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2010, 11, 13), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # We cannot add back in field 'Country.last_modified'
        raise RuntimeError(
            "Cannot reverse this migration. 'Country.last_modified' and its values cannot be restored.")

        # We cannot add back in field 'Country.pub_date'
        raise RuntimeError(
            "Cannot reverse this migration. 'Country.pub_date' and its values cannot be restored.")

        # Deleting field 'Country.created'
        db.delete_column('guides_country', 'created')

        # Deleting field 'Country.modified'
        db.delete_column('guides_country', 'modified')

        # We cannot add back in field 'Guide.last_modified'
        raise RuntimeError(
            "Cannot reverse this migration. 'Guide.last_modified' and its values cannot be restored.")

        # We cannot add back in field 'Guide.pub_date'
        raise RuntimeError(
            "Cannot reverse this migration. 'Guide.pub_date' and its values cannot be restored.")

        # Deleting field 'Guide.start_date'
        db.delete_column('guides_guide', 'start_date')

        # Deleting field 'Guide.end_date'
        db.delete_column('guides_guide', 'end_date')

        # Deleting field 'Guide.created'
        db.delete_column('guides_guide', 'created')

        # Deleting field 'Guide.modified'
        db.delete_column('guides_guide', 'modified')

        # We cannot add back in field 'City.last_modified'
        raise RuntimeError(
            "Cannot reverse this migration. 'City.last_modified' and its values cannot be restored.")

        # We cannot add back in field 'City.pub_date'
        raise RuntimeError(
            "Cannot reverse this migration. 'City.pub_date' and its values cannot be restored.")

        # Deleting field 'City.created'
        db.delete_column('guides_city', 'created')

        # Deleting field 'City.modified'
        db.delete_column('guides_city', 'modified')

        # We cannot add back in field 'Region.last_modified'
        raise RuntimeError(
            "Cannot reverse this migration. 'Region.last_modified' and its values cannot be restored.")

        # We cannot add back in field 'Region.pub_date'
        raise RuntimeError(
            "Cannot reverse this migration. 'Region.pub_date' and its values cannot be restored.")

        # Deleting field 'Region.created'
        db.delete_column('guides_region', 'created')

        # Deleting field 'Region.modified'
        db.delete_column('guides_region', 'modified')

        # We cannot add back in field 'Spot.last_modified'
        raise RuntimeError(
            "Cannot reverse this migration. 'Spot.last_modified' and its values cannot be restored.")

        # We cannot add back in field 'Spot.pub_date'
        raise RuntimeError(
            "Cannot reverse this migration. 'Spot.pub_date' and its values cannot be restored.")

        # Deleting field 'Spot.created'
        db.delete_column('guides_spot', 'created')

        # Deleting field 'Spot.modified'
        db.delete_column('guides_spot', 'modified')


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
        'guides.city': {
            'Meta': {'ordering': "('name',)", 'object_name': 'City'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Region']"}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'guides.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'guides.guide': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Guide'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'guides.guidelocationentry': {
            'Meta': {'object_name': 'GuideLocationEntry'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Guide']"})
        },
        'guides.guidespotentry': {
            'Meta': {'object_name': 'GuideSpotEntry'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.GuideLocationEntry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Spot']"})
        },
        'guides.region': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'guides.spot': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spot'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['guides.Region']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['guides']
