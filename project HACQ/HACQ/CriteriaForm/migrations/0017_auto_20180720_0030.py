# Generated by Django 2.0.7 on 2018-07-19 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0016_auto_20180719_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advanced_dimploma',
            name='form',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='form',
        ),
        migrations.RemoveField(
            model_name='diploma',
            name='form',
        ),
        migrations.RemoveField(
            model_name='innovative',
            name='form',
        ),
        migrations.DeleteModel(
            name='Institute',
        ),
        migrations.RemoveField(
            model_name='interdisciplinary',
            name='form',
        ),
        migrations.RemoveField(
            model_name='others',
            name='form',
        ),
        migrations.RemoveField(
            model_name='pg',
            name='form',
        ),
        migrations.RemoveField(
            model_name='pg_dimploma',
            name='form',
        ),
        migrations.RemoveField(
            model_name='phd',
            name='form',
        ),
        migrations.RemoveField(
            model_name='ug',
            name='form',
        ),
        migrations.DeleteModel(
            name='Advanced_Dimploma',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Diploma',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.DeleteModel(
            name='Innovative',
        ),
        migrations.DeleteModel(
            name='Interdisciplinary',
        ),
        migrations.DeleteModel(
            name='Others',
        ),
        migrations.DeleteModel(
            name='PG',
        ),
        migrations.DeleteModel(
            name='PG_Dimploma',
        ),
        migrations.DeleteModel(
            name='PhD',
        ),
        migrations.DeleteModel(
            name='UG',
        ),
    ]
