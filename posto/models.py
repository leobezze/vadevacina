# -*- coding: utf-8 -*-
from django.db import models


class Posto(models.Model):
    name_posto = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=150, blank=True)
 
    def __str__(self):
        return self.name_posto