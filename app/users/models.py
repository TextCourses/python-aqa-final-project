from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, blank=False, default='', unique=True)
    name = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=255, blank=False, default='')