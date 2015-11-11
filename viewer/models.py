# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class NycCensusBlocks(models.Model):
    gid = models.AutoField(primary_key=True)
    blkid = models.CharField(max_length=15, blank=True, null=True)
    popn_total = models.FloatField(blank=True, null=True)
    popn_white = models.FloatField(blank=True, null=True)
    popn_black = models.FloatField(blank=True, null=True)
    popn_nativ = models.FloatField(blank=True, null=True)
    popn_asian = models.FloatField(blank=True, null=True)
    popn_other = models.FloatField(blank=True, null=True)
    boroname = models.CharField(max_length=32, blank=True, null=True)
    geom = models.MultiPolygonField(srid=26918, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'nyc_census_blocks'


class NycHomicides(models.Model):
    gid = models.AutoField(primary_key=True)
    incident_d = models.DateField(blank=True, null=True)
    boroname = models.CharField(max_length=13, blank=True, null=True)
    num_victim = models.CharField(max_length=1, blank=True, null=True)
    primary_mo = models.CharField(max_length=20, blank=True, null=True)
    id = models.FloatField(blank=True, null=True)
    weapon = models.CharField(max_length=16, blank=True, null=True)
    light_dark = models.CharField(max_length=1, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    geom = models.PointField(srid=26918, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'nyc_homicides'


class NycNeighborhoods(models.Model):
    gid = models.AutoField(primary_key=True)
    boroname = models.CharField(max_length=43, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    geom = models.MultiPolygonField(srid=26918, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'nyc_neighborhoods'


class NycStreets(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    oneway = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiLineStringField(srid=26918, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'nyc_streets'


class NycSubwaystations(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=31, blank=True, null=True)
    alt_name = models.CharField(max_length=38, blank=True, null=True)
    cross_st = models.CharField(max_length=27, blank=True, null=True)
    long_name = models.CharField(max_length=60, blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    borough = models.CharField(max_length=15, blank=True, null=True)
    nghbhd = models.CharField(max_length=30, blank=True, null=True)
    routes = models.CharField(max_length=20, blank=True, null=True)
    transfers = models.CharField(max_length=25, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    express = models.CharField(max_length=10, blank=True, null=True)
    closed = models.CharField(max_length=10, blank=True, null=True)
    geom = models.PointField(srid=26918, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'nyc_subwaystations'
