# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    
class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course)
    created_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)