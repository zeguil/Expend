from django.db import models
from datetime import datetime


class Investimento(models.Model):
    investimento = models.TextField(max_length=200)
    valor = models.FloatField(max_length=9)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
