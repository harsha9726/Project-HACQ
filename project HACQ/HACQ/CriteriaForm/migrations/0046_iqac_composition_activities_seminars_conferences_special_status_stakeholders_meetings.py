# Generated by Django 2.0.7 on 2018-07-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0045_cycle1_cycle2_cycle3_cycle4'),
    ]

    operations = [
        migrations.CreateModel(
            name='IQAC_composition_activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers', models.IntegerField()),
                ('administrative_staff', models.IntegerField()),
                ('students', models.IntegerField()),
                ('management_representatives', models.IntegerField()),
                ('alumni', models.IntegerField()),
                ('stakeholder_community_representatives', models.IntegerField()),
                ('employers_industrialists', models.IntegerField()),
                ('external_experts', models.IntegerField()),
                ('total_members', models.IntegerField()),
                ('iqac_meetings_held', models.IntegerField()),
                ('funding_received', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('funding_amount', models.IntegerField()),
                ('activites_contributions', models.TextField()),
                ('plan_of_action', models.TextField()),
                ('achivements_by_year', models.TextField()),
                ('aqar_statutory_body', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('aqar_statutory_body_yes', models.CharField(choices=[('M', 'Management'), ('S', 'Syndicate'), ('O', 'Other')], max_length=1, null=True)),
                ('plan_of_action_taken', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seminars_conferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('international', models.IntegerField()),
                ('national', models.IntegerField()),
                ('state', models.IntegerField()),
                ('institute', models.IntegerField()),
                ('themes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Special_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autonomy', models.CharField(max_length=100)),
                ('university_excellence', models.CharField(max_length=100)),
                ('dst_star_schema', models.CharField(max_length=100)),
                ('ugc_sap', models.CharField(max_length=100)),
                ('ugc_ipp', models.CharField(max_length=100)),
                ('ugc_cop', models.CharField(max_length=100)),
                ('ugc_cpe', models.CharField(max_length=100)),
                ('ugc_ce', models.CharField(max_length=100)),
                ('dst_fist', models.CharField(max_length=100)),
                ('others', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholders_meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('faculty', models.IntegerField()),
                ('nonteaching_staff_students', models.IntegerField()),
                ('alumni', models.IntegerField()),
                ('others', models.IntegerField()),
            ],
        ),
    ]
