# Generated by Django 3.1.2 on 2020-10-20 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='data_servico',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 5, 54, 39, 785227, tzinfo=utc), verbose_name='data do serviço'),
        ),
    ]
