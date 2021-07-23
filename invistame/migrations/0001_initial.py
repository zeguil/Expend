# Generated by Django 3.1.7 on 2021-07-20 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investimento', models.TextField(max_length=200)),
                ('valor', models.FloatField(max_length=9)),
                ('pago', models.BooleanField(default=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]