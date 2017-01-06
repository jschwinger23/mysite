from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Entries(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)

    class Meta:
        db_table = 'entries'


