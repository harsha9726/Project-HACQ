# Generated by Django 2.0.7 on 2018-07-16 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0008_auto_20180716_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]
