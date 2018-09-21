from . import models as m
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

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


#####=====================Criteria 1 forms=============########
class Criteria1Form(ModelForm):
    class Meta:
        model = m.Criteria1
        fields = ['semester','trimester','annual','revision_update_syllabi','Department_center','Feedback_stakeholders','Mode_of_feedback']
class PhDForm(ModelForm):
    class Meta:
        model = m.PhD
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class PGForm(ModelForm):
    class Meta:
        model = m.PG
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class UGForm(ModelForm):
    class Meta:
        model = m.UG
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class PG_DiplomaForm(ModelForm):
    class Meta:
        model = m.PG_Diploma
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class Advanced_DiplomaForm(ModelForm):
    class Meta:
        model = m.Advanced_Diploma
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class DiplomaForm(ModelForm):
    class Meta:
        model = m.Diploma
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class CertificateForm(ModelForm):
    class Meta:
        model = m.Certificate
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class OthersForm(ModelForm):
    class Meta:
        model = m.Others
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class InterdisciplinaryForm(ModelForm):
    class Meta:
        model = m.Interdisciplinary
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class InnovativeForm(ModelForm):
    class Meta:
        model = m.Innovative
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']
class TotalForm(ModelForm):
    class Meta:
        model = m.Total
        fields = ['Number_of_existing_programmes','Number_of_programmes_added_during_year','Number_of_self_financing_programmes','Number_of_value_added_career_Oriented_programmes']

#####=====================Criteria 2 forms=============########
class Criteria2Form(ModelForm):
    class Meta:
        model = m.Criteria2
        fields = ['permanent_phd','guest_faculty','visiting_faculty','temporary_faculty','innovative_processes_introduced','teaching_days',
                    'examination_evaluation_reforms_introduced','faculty_restructuring','faculty_revision','faculty_syllabus_development',
                    'average_attendance_students','iqac_evaluation_teaching_learning_process','refresher_courses','UGC_faculty_improvement_programme',
                    'HRD_programmes','orientation_programmes','faculty_exchange_programmes','staff_training_university','staff_training_institutions',
                    'summer_winter_schools_workshops','others']
class Permanent_facultyForm(ModelForm):
    class Meta:
        model = m.Permanent_faculty
        fields = ['total','asst_professors','associate_professors','professors','others']
class Faculty_PositionsForm(ModelForm):
    class Meta:
        model = m.Faculty_Positions
        fields = ['asst_professor_recruited','asst_professor_vacant','associate_professor_recruited','associate_professor_vacant','professor_recruited',
                    'professor_vacant','others_recruited','others_vacant','total_recruited','total_vacant']
class Faculty_attendedForm(ModelForm):
    class Meta:
        model = m.Faculty_attended
        fields = ['international','national','state']
class Faculty_Presented_PapersForm(ModelForm):
    class Meta:
        model = m.Faculty_Presented_Papers
        fields = ['international','national','state']
class Faculty_Resources_PersonsForm(ModelForm):
    class Meta:
        model = m.Faculty_Resources_Persons
        fields = ['international','national','state']
class Course_programme_distribution_of_percentageForm(ModelForm):
    class Meta:
        model = m.Course_programme_distribution_of_percentage
        fields = ['title','total_no_of_students_appeared','distinction','first','second','third','pass_p','form_serial']
class Administrative_staffForm(ModelForm):
    class Meta:
        model = m.Administrative_staff
        fields = ['permanent_employees','vacant_positions','permanent_positions_filled','positions_filled_temporarily']
class Technical_staffForm(ModelForm):
    class Meta:
        model = m.Technical_staff
        fields = ['permanent_employees','vacant_positions','permanent_positions_filled','positions_filled_temporarily']

#####=====================Criteria 3 forms=============########
class Criteria3Form(ModelForm):
    class Meta:
        model = m.Criteria3
        fields = ['promoting_research','impactfactor_range','impactfactor_average','impactfactor_h_index','impactfactor_nos_in_scopus','books_isbn',
                    'books_non_isbn','books_chapters_edited_books','revenue_consultancy','faculty_experts_chair_resource_persons',
                    'collaborations_international','collaborations_national','collaborations_other','linkages_created']
class Major_projectsForm(ModelForm):
    class Meta:
        model = m.Major_projects
        fields = ['number_completed','number_ongoing','number_sanctioned','number_submitted','outlay_completed','outlay_ongoing','outlay_sanctioned',
                    'outlay_submitted']
class Minor_projectsForm(ModelForm):
    class Meta:
        model = m.Minor_projects
        fields = ['number_completed','number_ongoing','number_sanctioned','number_submitted','outlay_completed','outlay_ongoing','outlay_sanctioned',
                    'outlay_submitted']
class Research_publicationsForm(ModelForm):
    class Meta:
        model = m.Research_publications
        fields = ['peer_review_journals_international','peer_review_journals_national','peer_review_journals_others','non_peer_review_journals_international',
                    'non_peer_review_journals_national','non_peer_review_journals_others','e_journals_international','e_journals_national','e_journals_others',
                    'conference_proceedings_international','conference_proceedings_national','conference_proceedings_others']
class University_department_fundsForm(ModelForm):
    class Meta:
        model = m.University_department_funds
        fields = ['ugc_sap','cas','dst_fist','dpe','dbt_scheme_funds']
class Funds_For_collegesForm(ModelForm):
    class Meta:
        model = m.Funds_For_colleges
        fields = ['autonomy','cpe','dbt_star_scheme','inspire','ce','others']
class Conferences_organized_institutionForm(ModelForm):
    class Meta:
        model = m.Conferences_organized_institution
        fields = ['number_international','number_national','number_state','number_university','number_college','sponsor_international','sponsor_national',
                    'sponsor_state','sponsor_university','sponsor_college']
