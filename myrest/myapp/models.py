# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

