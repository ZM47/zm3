# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class DjangoMigrations(models.Model):
   app = models.CharField(max_length=255)
   name = models.CharField(max_length=255)
   applied = models.DateTimeField()

class Meta:
       managed = False
       db_table = 'django_migrations'


class Doubans(models.Model):


    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doubans'


class Ordinarymember(models.Model):

     用户 = models.OneToOneField(User,on_delete=models.CASCADE)
     昵称 = models.CharField(max_length=50,blank=True)
     生日 = models.CharField(max_length=50,blank=True,null=True)

     class Meta:
         verbose_name_plural = "ordinarymembers"

class Biancheng(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biancheng'


class Keji(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keji'

