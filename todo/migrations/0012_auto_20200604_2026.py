# Generated by Django 3.0.5 on 2020-06-04 11:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20200604_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Todo_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 4, 11, 26, 46, 115072, tzinfo=utc), null=True),
        ),
    ]
