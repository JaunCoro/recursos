# Generated by Django 2.0.3 on 2019-06-03 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190602_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='salida',
            field=models.CharField(default=datetime.datetime(2019, 6, 3, 7, 20, 26, 371983), max_length=150),
        ),
    ]