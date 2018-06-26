# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DistinctRides(models.Model):
    distinct_rides = models.IntegerField(primary_key=True)
    cust_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distinct_rides'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Eda1(models.Model):
    field_usageid = models.IntegerField(db_column='\ufeffusageid', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    usetime = models.DateTimeField(blank=True, null=True)
    accesscode = models.IntegerField(blank=True, null=True)
    visualid = models.FloatField(blank=True, null=True)
    rideid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    useno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_1'


class Eda2(models.Model):
    usageid = models.IntegerField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    accesscode = models.IntegerField(blank=True, null=True)
    visualid = models.BigIntegerField(blank=True, null=True)
    rideid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    useno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_2'


class MallMinutes(models.Model):
    miniutes_in_mall = models.IntegerField(primary_key=True)
    cust_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_minutes'


class MasterUsage(models.Model):
    usgeid = models.FloatField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    accesscode = models.FloatField(blank=True, null=True)
    visualid = models.FloatField(blank=True, null=True)
    rideid = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    useno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_usage'


class PathProb(models.Model):
    ride1 = models.CharField(primary_key=True, max_length=50)
    ride2 = models.CharField(max_length=50)
    cust_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'path_prob'
        unique_together = (('ride1', 'ride2'),)


class RideCount(models.Model):
    no_of_rides = models.IntegerField(primary_key=True)
    cust_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ride_count'


class Ridestable(models.Model):
    field_rideid = models.IntegerField(db_column='\ufeffRideID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    longname = models.TextField(db_column='LongName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ridestable'


class Sunburst(models.Model):
    category = models.CharField(db_column='Category', primary_key=True, max_length=20)  # Field name made lowercase.
    ride = models.CharField(db_column='Ride', max_length=20)  # Field name made lowercase.
    hr = models.IntegerField()
    cust_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sunburst'
        unique_together = (('category', 'ride', 'hr'),)


class Ticketcategories(models.Model):
    field_accesscodeid = models.IntegerField(db_column='\ufeffAccessCodeID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    subcategory = models.TextField(db_column='Subcategory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticketcategories'


class Tickets(models.Model):
    ticket_type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    ticketname = models.CharField(primary_key=True, max_length=50)
    size = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'
