# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Layman(models.Model):
    ID = models.AutoField(primary_key = True)
    schoolID = models.CharField(max_length = 12)
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 5)
    college = models.CharField(max_length = 100)
    QQnumber = models.CharField(max_length =15)
    dorm = models.CharField(max_length = 10)
    telephone = models.CharField(max_length = 11)
    department1 = models.CharField(max_length = 50)
    department2 = models.CharField(max_length = 50,default = "")
    adjust = models.CharField(max_length = 5)
    degree = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    introduce = models.CharField(max_length = 1000)
    register_time = models.DateTimeField(auto_now_add = True)
    interview = models.CharField(max_length = 30,default="")
    passed = models.IntegerField(default = -1)
    department = models.CharField(max_length = 30,default = "")
    applydate = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class NorthCampus(models.Model):
    ID = models.AutoField(primary_key = True)
    schoolID = models.CharField(max_length = 12)
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 5)
    college = models.CharField(max_length = 100)
    QQnumber = models.CharField(max_length =15)
    dorm = models.CharField(max_length = 10)
    telephone = models.CharField(max_length = 11)
    department1 = models.CharField(max_length = 50)
    department2 = models.CharField(max_length = 50,default = "")
    adjust = models.CharField(max_length = 5)
    degree = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    register_time = models.DateTimeField(auto_now_add = True)
    interview = models.CharField(max_length = 30,default="")
    passed = models.IntegerField(default = -1)
    department = models.CharField(max_length = 30,default = "")

    professor_name = models.CharField(max_length = 30)
    professor_major = models.CharField(max_length = 30)
    aimat = models.CharField(max_length = 30)
    monologue = models.CharField(max_length = 500)
    habbit = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 100)
    keypoint = models.CharField(max_length = 1000)
    whyjoin = models.CharField(max_length = 1000)
    whychoose = models.CharField(max_length = 1000)

class CC(models.Model):
    ID = models.AutoField(primary_key = True)
    schoolID = models.CharField(max_length = 12)
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 5)
    QQnumber = models.CharField(max_length =15)
    dorm = models.CharField(max_length = 10)
    telephone = models.CharField(max_length = 11)
    classes = models.CharField(max_length = 30)
    leader = models.CharField(max_length = 5)
    email = models.CharField(max_length = 30)
    introduce = models.CharField(max_length = 1000)
    register_time = models.DateTimeField(auto_now_add = True)
    interview = models.CharField(max_length = 30,default="")
    passed = models.IntegerField(default = -1)
    department = models.CharField(max_length = 30,default = "")
    applydate = models.DateField(auto_now_add=True)