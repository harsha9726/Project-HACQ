# Generated by Django 2.0.7 on 2018-07-23 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0023_auto_20180723_1757'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cycle1',
        ),
        migrations.DeleteModel(
            name='Cycle2',
        ),
        migrations.DeleteModel(
            name='Cycle3',
        ),
        migrations.DeleteModel(
            name='Cycle4',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='form',
        ),
        migrations.RemoveField(
            model_name='iqac_composition_activities',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='seminars_conferences',
            name='IQAC_composition_activities',
        ),
        migrations.RemoveField(
            model_name='special_status',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='stakeholders_meetings',
            name='IQAC_composition_activities',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.DeleteModel(
            name='Institute',
        ),
        migrations.DeleteModel(
            name='IQAC_composition_activities',
        ),
        migrations.DeleteModel(
            name='Seminars_conferences',
        ),
        migrations.DeleteModel(
            name='Special_status',
        ),
        migrations.DeleteModel(
            name='Stakeholders_meetings',
        ),
    ]
