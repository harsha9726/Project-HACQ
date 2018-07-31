# Generated by Django 2.0.7 on 2018-07-19 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CriteriaForm', '0017_auto_20180720_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, verbose_name='date created')),
            ],
        ),
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
                ('naac_track_id', models.CharField(max_length=20)),
                ('naac_executive_committe_date', models.CharField(max_length=50)),
                ('college_website', models.URLField()),
                ('aqar_weblink', models.URLField()),
                ('date_of_iqac_establishment', models.DateField()),
                ('aqar_submission_1', models.CharField(max_length=100)),
                ('aqar_submission_2', models.CharField(max_length=100)),
                ('aqar_submission_3', models.CharField(max_length=100)),
                ('aqar_submission_4', models.CharField(max_length=100)),
                ('university', models.CharField(choices=[('S', 'State'), ('C', 'Central'), ('D', 'Deemed'), ('P', 'Private')], max_length=2)),
                ('Affiliated', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('Constituent', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('autonomous', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('regulatory_agency_approved', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('type_of_institution', models.CharField(choices=[('CO', 'Co-education'), ('M', 'Men'), ('W', 'Women'), ('U', 'Urban'), ('R', 'Rural'), ('T', 'Tribal')], max_length=2)),
                ('financial_status', models.CharField(choices=[('G', 'Grant-in-aid'), ('UF', 'UGC 2(f)'), ('UG', 'UGC 12B'), ('GS', 'Grant-in-aid + Self Financing'), ('TS', 'Totally Self-financing')], max_length=3)),
                ('type_of_faculty', models.CharField(choices=[('A', 'Arts'), ('S', 'Science'), ('C', 'Commerce'), ('L', 'Law'), ('P', 'PIE'), ('T', 'TEI'), ('E', 'Engineering'), ('HS', 'Health Science'), ('M', 'Management')], max_length=2)),
                ('type_of_faculty_others', models.CharField(max_length=100)),
                ('affiliating_univercity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Institute_accreditation_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.CharField(max_length=30)),
                ('grade', models.IntegerField()),
                ('year_of_accreditation', models.IntegerField()),
                ('validity_period', models.IntegerField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CriteriaForm.Institute')),
            ],
        ),
    ]
