from datetime import datetime
from django.db import models
from django.db.models.fields import CharField, DateTimeField


# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=20)
    cep = models.CharField(max_length=15)
    data = models.DateTimeField()

class Medicos(models.Model):
    nome = CharField(max_length=60)
    email = CharField(max_length=60)
    senha = CharField(max_length=60)
    data = DateTimeField()