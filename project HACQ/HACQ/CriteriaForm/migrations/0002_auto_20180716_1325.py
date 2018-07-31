# Generated by Django 2.0.7 on 2018-07-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('college_id', models.CharField(max_length=10)),
                ('Number_of_existing_programmes', models.IntegerField()),
                ('Number_of_programmes_added_during_year', models.IntegerField()),
                ('Number_of_self_financing_programmes', models.IntegerField()),
                ('Number_of_value_added_career_Oriented_programmes', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Academic_Programmes',
        ),
    ]
