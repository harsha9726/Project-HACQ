# Generated by Django 2.0.7 on 2018-07-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0015_auto_20180716_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address_line_1', models.CharField(max_length=1000)),
                ('address_line_2', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('college_email_address', models.EmailField(max_length=254)),
                ('head_of_institute', models.CharField(max_length=200)),
                ('telephone', models.PositiveIntegerField()),
                ('college_mobile', models.IntegerField()),
                ('iqac_coordinator', models.CharField(max_length=200)),
                ('coordinator_mobile', models.IntegerField()),
                ('iqac_email', models.EmailField(max_length=254)),
                ('faculty_name', models.CharField(max_length=100)),
                ('college_id', models.CharField(max_length=10)),
                ('branch_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='form',
            name='branch_id',
        ),
        migrations.RemoveField(
            model_name='form',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='form',
            name='faculty_name',
        ),
    ]
