from django.db import models
from django.utils import timezone
import time

from django.db.models.fields import DateTimeField

class CategoriaGasto(models.Model):
    nome = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome


class Gasto(models.Model):
    gasto = models.TextField(max_length=200)
    valor = models.FloatField(max_length=9)
    pago = models.BooleanField(default=False)
    data = models.DateTimeField(default=timezone.now)
    hora = models.TimeField(default=time.strftime('%H:%M', time.localtime()))
    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.gasto

class CategoriaContato(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=80, blank=True)
    telefone = models.CharField(max_length=13, default=None)
    aniversario = models.DateField(default=None)
    email  = models.CharField(max_length=80)
    descricao = models.TextField(max_length=100, blank=True)
    categoria = models.ForeignKey(CategoriaContato, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.nome