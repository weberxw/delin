# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Resume(models.Model):

    class Meta:

        db_table = 'resume'

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Myrest(models.Model):
    
    class Meta:
        permissions = (
            ('view_userprofile', 'View UserProfile'),
        )
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='profile')
    description = models.CharField(max_length=30)
    done = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)