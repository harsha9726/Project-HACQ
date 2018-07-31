# Generated by Django 2.0.7 on 2018-07-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CriteriaForm', '0030_auto_20180728_1154'),
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
        migrations.RemoveField(
            model_name='institute',
            name='Affiliated',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='Constituent',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='affiliating_university',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_for_year',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_submission_1',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_submission_2',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_submission_3',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_submission_4',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='aqar_weblink',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='autonomous',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='city',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='college_contact_no',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='college_email_address',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='college_mobile',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='college_website',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='coordinator_mobile',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='date_of_iqac_establishment',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='financial_status',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='head_of_institute',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='iqac_coordinator',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='iqac_email',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='iqac_funding',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='iqac_funding_amount',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='naac_executive_committe_date',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='naac_track_id',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='regulatory_agency_approved',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='state',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='type_of_faculty',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='type_of_faculty_others',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='type_of_institution',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='university',
        ),
    ]
