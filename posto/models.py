# -*- coding: utf-8 -*-
from django.db import models


class Posto(models.Model):
    name_posto = models.CharField('Nome do Posto',max_length=255, blank=False)
    cnes = models.CharField('CNES',max_length=255, blank=False)
    slug = models.SlugField('Identificador', max_length=100)
    address = models.TextField('Endereço',blank=True)
 
    def __str__(self):
        return self.name_posto

class Vacina(models.Model):
    name_vacina = models.CharField('Nome da Vacina',max_length=255, blank=False)
    lote = models.CharField('Lote',max_length=255, blank=False)
    resonsavel = models.CharField('responsavel',max_length=255, blank=False)
 
    def __str__(self):
        return self.name_vacina