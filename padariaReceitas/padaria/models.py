from django.db import models


class Receita(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=266, null=False, blank=False)
