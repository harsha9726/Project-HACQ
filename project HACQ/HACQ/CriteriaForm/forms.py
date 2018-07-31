from . import models as m
from django.forms import ModelForm

class InstituteForm(ModelForm):
    class Meta:
        model = m.Institute
        fields = ['name','address_line_1','address_line_2','city','state','pincode',
        'college_email_address','college_contact_no',
        'head_of_institute','telephone','college_mobile','iqac_coordinator','coordinator_mobile','iqac_email',
        'naac_track_id','naac_executive_committe_date','college_website','aqar_weblink','date_of_iqac_establishment',
        'aqar_for_year','aqar_submission_1','aqar_submission_2','aqar_submission_3','aqar_submission_4','university','Affiliated',
        'Constituent','autonomous','regulatory_agency_approved','type_of_institution','financial_status',
        'type_of_institution','type_of_faculty','type_of_faculty_others','affiliating_university','iqac_funding','iqac_funding_amount']

class Cycle1Form(ModelForm):
    class Meta:
        model = m.Cycle1
        fields = ['grade','cgpa','year_of_accreditation','validity_period']
class Cycle2Form(ModelForm):
    class Meta:
        model = m.Cycle2
        fields = ['grade','cgpa','year_of_accreditation','validity_period']
class Cycle3Form(ModelForm):
    class Meta:
        model = m.Cycle3
        fields = ['grade','cgpa','year_of_accreditation','validity_period']
class Cycle4Form(ModelForm):
    class Meta:
        model = m.Cycle4
        fields = ['grade','cgpa','year_of_accreditation','validity_period']
class Special_statusForm(ModelForm):
    class Meta:
        model = m.Special_status
        fields = ['autonomy','university_excellence','dst_star_schema','ugc_sap','ugc_ipp','ugc_cop','ugc_cpe',
        'ugc_ce','dst_fist','others']
class IQAC_composition_activitiesForm(ModelForm):
    class Meta:
        model = m.IQAC_composition_activities
        fields = ['teachers','administrative_staff','students','management_representatives','alumni','stakeholder_community_representatives',
        'employers_industrialists','external_experts','total_members','iqac_meetings_held','activites_contributions','funding_received','funding_amount','plan_of_action',
        'achivements_by_year','aqar_statutory_body','aqar_statutory_body_yes','plan_of_action_taken']
class Stakeholders_meetingsForm(ModelForm):
    class Meta:
        model = m.Stakeholders_meetings
        fields = ['total','faculty','nonteaching_staff_students','alumni','others']
class Seminars_conferencesForm(ModelForm):
    class Meta:
        model = m.Seminars_conferences
        fields = ['total','international','national','state','institute','themes']
