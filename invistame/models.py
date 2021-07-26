from django.db import models
from datetime import datetime
import time

from django.db.models.fields import DateTimeField


class Investimento(models.Model):
    investimento = models.TextField(max_length=200)
    valor = models.FloatField(max_length=9)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    hora = models.TimeField(default=time.strftime('%H:%M', time.localtime()))
