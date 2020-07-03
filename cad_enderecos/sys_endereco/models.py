# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Endereco(models.Model):
    cep = models.CharField(primary_key=True, max_length=8)
    logradouro = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=45)
    uf = models.CharField(max_length=2)
    complemento = models.CharField(max_length=45, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'
