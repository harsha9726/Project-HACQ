# Generated by Django 2.0.7 on 2018-07-28 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0040_auto_20180728_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='date_of_iqac_establishment',
        ),
    ]
