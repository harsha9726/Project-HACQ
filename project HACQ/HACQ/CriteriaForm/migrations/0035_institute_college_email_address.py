# Generated by Django 2.0.7 on 2018-07-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0034_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='college_email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
