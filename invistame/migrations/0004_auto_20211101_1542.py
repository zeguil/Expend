# Generated by Django 3.2.5 on 2021-11-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invistame', '0003_investimento_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(blank=True, max_length=80)),
                ('email', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='investimento',
            name='hora',
            field=models.TimeField(default='15:42'),
        ),
    ]
