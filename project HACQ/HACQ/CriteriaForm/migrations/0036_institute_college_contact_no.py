# Generated by Django 2.0.7 on 2018-07-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0035_institute_college_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='college_contact_no',
            field=models.IntegerField(null=True),
        ),
    ]
