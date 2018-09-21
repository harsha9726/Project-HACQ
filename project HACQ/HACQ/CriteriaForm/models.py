from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

# Create your models here.

class Form(models.Model):
    create_date = models.DateTimeField('date created',auto_now_add=True,blank=True)
    department = models.CharField(max_length=10,null=True)

####=============================Institutional Details models==========================#

class Institute(models.Model):
    #form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=1000)
    address_line_2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    college_email_address = models.EmailField(null=True)
    college_contact_no = models.BigIntegerField(null=True)
    head_of_institute = models.CharField(max_length=200,null=True)
    telephone = models.BigIntegerField(null=True)
    college_mobile = models.BigIntegerField(null=True)
    iqac_coordinator = models.CharField(max_length=200,null=True)
    coordinator_mobile = models.BigIntegerField(null=True)
    iqac_email = models.EmailField(null=True)
    naac_track_id = models.CharField(max_length = 200,null=True)
    naac_executive_committe_date = models.CharField(max_length = 500,null=True)
    college_website = models.URLField(null=True)
    aqar_weblink = models.URLField(null=True)
    date_of_iqac_establishment = models.CharField(max_length=200,null=True)
    aqar_for_year = models.CharField(max_length=100,null=True)
    aqar_submission_1 = models.CharField(max_length = 100,null=True)
    aqar_submission_2 = models.CharField(max_length = 100,null=True)
    aqar_submission_3 = models.CharField(max_length = 100,null=True)
    aqar_submission_4 = models.CharField(max_length = 100,null=True)
    university = models.CharField(max_length=2,null=True,choices=(('S','State'),
                                                        ('C','Central'),
                                                        ('D','Deemed'),
                                                        ('P','Private')))
    Affiliated = models.CharField(max_length=2,null=True,choices=(('Y','Yes'),('N','No')))
    Constituent = models.CharField(max_length=2,null=True,choices=(('Y','Yes'),('N','No')))
    autonomous = models.CharField(max_length=2,null=True,choices=(('Y','Yes'),('N','No')))
    regulatory_agency_approved = models.CharField(max_length=2,null=True,choices=(('Y','Yes'),('N','No')))
    type_of_institution = models.CharField(max_length=4,null=True,choices=(('CO','Co-education'),
                                                                 ('M','Men'),('W','Women'),
                                                                 ('U','Urban'),('R','Rural'),
                                                                 ('T','Tribal')))
    financial_status = models.CharField(max_length=3,null=True,choices=(('G','Grant-in-aid'),
                                                              ('UF','UGC 2(f)'),
                                                              ('UG','UGC 12B'),
                                                              ('GS','Grant-in-aid + Self Financing'),
                                                              ('TS','Totally Self-financing')))
    type_of_faculty = models.CharField(max_length=2,null=True,choices=(('A','Arts'),
                                                             ('S','Science'),
                                                             ('C','Commerce'),
                                                             ('L','Law'),
                                                             ('P','PIE'),
                                                             ('T','TEI'),
                                                             ('E','Engineering'),
                                                             ('HS','Health Science'),
                                                             ('M','Management'),
                                                             ('O','Others')))
    type_of_faculty_others = models.CharField(max_length=100,null=True)
    affiliating_university = models.CharField(max_length=200,null=True)
    iqac_funding = models.CharField(max_length=4,null=True,choices=(('Y','Yes'),('N','No')))
    iqac_funding_amount = models.BigIntegerField(null=True)

class Cycle1(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    grade = models.IntegerField()
    cgpa = models.CharField(max_length=10)
    year_of_accreditation = models.IntegerField()
    validity_period = models.IntegerField()
class Cycle2(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    grade = models.IntegerField()
    cgpa = models.CharField(max_length=10)
    year_of_accreditation = models.IntegerField()
    validity_period = models.IntegerField()
class Cycle3(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    grade = models.IntegerField()
    cgpa = models.CharField(max_length=10)
    year_of_accreditation = models.IntegerField()
    validity_period = models.IntegerField()
class Cycle4(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    grade = models.IntegerField()
    cgpa = models.CharField(max_length=10)
    year_of_accreditation = models.IntegerField()
    validity_period = models.IntegerField()

class Special_status(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    autonomy = models.CharField(max_length = 100)
    university_excellence = models.CharField(max_length = 100)
    dst_star_schema = models.CharField(max_length = 100)
    ugc_sap = models.CharField(max_length = 100)
    ugc_ipp = models.CharField(max_length = 100)
    ugc_cop = models.CharField(max_length = 100)
    ugc_cpe = models.CharField(max_length = 100)
    ugc_ce = models.CharField(max_length = 100)
    dst_fist = models.CharField(max_length = 100)
    others = models.TextField()

class IQAC_composition_activities(models.Model):
    #institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    teachers = models.IntegerField()
    administrative_staff = models.IntegerField()
    students = models.IntegerField()
    management_representatives = models.IntegerField()
    alumni = models.IntegerField()
    stakeholder_community_representatives = models.IntegerField()
    employers_industrialists = models.IntegerField()
    external_experts = models.IntegerField()
    total_members = models.IntegerField()
    iqac_meetings_held = models.IntegerField()
    funding_received = models.CharField(max_length=1,choices=(('Y','Yes'),('N','No')))
    funding_amount = models.IntegerField()
    activites_contributions = models.TextField()
    plan_of_action = models.TextField()
    achivements_by_year = models.TextField()
    aqar_statutory_body = models.CharField(max_length=1,choices=(('Y','Yes'),('N','No')))
    aqar_statutory_body_yes = models.CharField(max_length=1,null=True,choices=(('M','Management'),
                                                                               ('S','Syndicate'),
                                                                               ('O','Other')))
    plan_of_action_taken = models.TextField()

class Stakeholders_meetings(models.Model):
    #IQAC_composition_activities = models.ForeignKey(IQAC_composition_activities,on_delete=models.CASCADE)
    total = models.IntegerField()
    faculty = models.IntegerField()
    nonteaching_staff_students = models.IntegerField()
    alumni = models.IntegerField()
    others = models.IntegerField()

class Seminars_conferences(models.Model):
    #IQAC_composition_activities = models.ForeignKey(IQAC_composition_activities,on_delete=models.CASCADE)
    total = models.IntegerField()
    international = models.IntegerField()
    national = models.IntegerField()
    state = models.IntegerField()
    institute = models.IntegerField()
    themes = models.TextField()



####==================================Criteria 1 models==============================#


class Criteria1(models.Model):
    semester = models.IntegerField()
    trimester = models.IntegerField()
    annual = models.IntegerField()
    revision_update_syllabi = models.TextField()
    Department_center = models.TextField()
    Feedback_stakeholders = MultiSelectField(null=True,choices=(('A','Alumni'),('P','Parents'),
                                                            ('E','Employers'),('S','Students')))
    Mode_of_feedback = MultiSelectField(null=True,choices=(('O','Online'),('M','Manual'),('C','Co-operating schools(for PEI)')))

class PhD(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class PG(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class UG(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class PG_Diploma(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Advanced_Diploma(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Diploma(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Certificate(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Others(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Interdisciplinary(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Innovative(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Total(models.Model):
    #Criteria1 = models.ForeignKey(Criteria1, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()



#####===================================Criteria 2==========================#####


class Criteria2(models.Model):
    permanent_phd = models.IntegerField()
    guest_faculty = models.IntegerField()
    visiting_faculty = models.IntegerField()
    temporary_faculty = models.IntegerField()
    innovative_processes_introduced = models.TextField()
    teaching_days = models.IntegerField()
    examination_evaluation_reforms_introduced = models.IntegerField()
    faculty_restructuring = models.IntegerField()
    faculty_revision = models.IntegerField()
    faculty_syllabus_development = models.IntegerField()
    average_attendance_students = models.IntegerField()
    iqac_evaluation_teaching_learning_process = models.TextField()
    #faculty_development = models.TextField()
    refresher_courses = models.IntegerField()
    UGC_faculty_improvement_programme = models.IntegerField()
    HRD_programmes = models.IntegerField()
    orientation_programmes = models.IntegerField()
    faculty_exchange_programmes = models.IntegerField()
    staff_training_university = models.IntegerField()
    staff_training_institutions = models.IntegerField()
    summer_winter_schools_workshops = models.IntegerField()
    others = models.IntegerField()

class Permanent_faculty(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    total = models.IntegerField()
    asst_professors = models.IntegerField()
    associate_professors = models.IntegerField()
    professors = models.IntegerField()
    others = models.IntegerField()

class Faculty_Positions(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    asst_professor_recruited = models.IntegerField()
    asst_professor_vacant = models.IntegerField()
    associate_professor_recruited = models.IntegerField()
    associate_professor_vacant = models.IntegerField()
    professor_recruited = models.IntegerField()
    professor_vacant = models.IntegerField()
    others_recruited = models.IntegerField()
    others_vacant = models.IntegerField()
    total_recruited = models.IntegerField()
    total_vacant = models.IntegerField()

class Faculty_attended(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    international = models.IntegerField()
    national = models.IntegerField()
    state = models.IntegerField()

class Faculty_Presented_Papers(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    international = models.IntegerField()
    national = models.IntegerField()
    state = models.IntegerField()

class Faculty_Resources_Persons(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    international = models.IntegerField()
    national = models.IntegerField()
    state = models.IntegerField()

class Course_programme_distribution_of_percentage(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_no_of_students_appeared = models.IntegerField()
    distinction = models.IntegerField()
    first = models.IntegerField()
    second = models.IntegerField()
    third = models.IntegerField()
    pass_p = models.IntegerField()
    form_serial = models.IntegerField()

class Administrative_staff(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    permanent_employees = models.IntegerField()
    vacant_positions = models.IntegerField()
    permanent_positions_filled = models.IntegerField()
    positions_filled_temporarily = models.IntegerField()

class Technical_staff(models.Model):
    #Criteria2 = models.ForeignKey(Criteria2, on_delete=models.CASCADE)
    permanent_employees = models.IntegerField()
    vacant_positions = models.IntegerField()
    permanent_positions_filled = models.IntegerField()
    positions_filled_temporarily = models.IntegerField()

########=========================Criteria 3=============================##########

class Criteria3(models.Model):
    promoting_research = models.TextField()
    impactfactor_range = models.IntegerField()
    impactfactor_average = models.IntegerField()
    impactfactor_h_index = models.IntegerField()
    impactfactor_nos_in_scopus = models.IntegerField()
    books_isbn = models.IntegerField()
    books_non_isbn = models.IntegerField()
    books_chapters_edited_books = models.IntegerField()
    revenue_consultancy = models.IntegerField()
    faculty_experts_chair_resource_persons = models.IntegerField()
    collaborations_international = models.IntegerField()
    collaborations_national = models.IntegerField()
    collaborations_other = models.IntegerField()
    linkages_created = models.IntegerField()
    budget_funding_agency = models.IntegerField()
    budget_management = models.IntegerField()
    budget_total = models.IntegerField()
    phd_guides = models.IntegerField()
    students_under_phd = models.IntegerField()
    phd_awarded = models.IntegerField()
    scholar_jrf = models.IntegerField()
    scholar_srf = models.IntegerField()
    scholar_project_fellows = models.IntegerField()
    scholar_other = models.IntegerField()
    major_activities_1 = models.TextField()
    major_activities_2 = models.TextField()

class Major_projects(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    number_completed = models.IntegerField()
    number_ongoing = models.IntegerField()
    number_sanctioned = models.IntegerField()
    number_submitted = models.IntegerField()
    outlay_completed = models.IntegerField()
    outlay_ongoing = models.IntegerField()
    outlay_sanctioned = models.IntegerField()
    outlay_submitted = models.IntegerField()

class Minor_projects(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    number_completed = models.IntegerField()
    number_ongoing = models.IntegerField()
    number_sanctioned = models.IntegerField()
    number_submitted = models.IntegerField()
    outlay_completed = models.IntegerField()
    outlay_ongoing = models.IntegerField()
    outlay_sanctioned = models.IntegerField()
    outlay_submitted = models.IntegerField()

class Research_publications(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    peer_review_journals_international = models.IntegerField()
    peer_review_journals_national = models.IntegerField()
    peer_review_journals_others = models.IntegerField()
    non_peer_review_journals_international = models.IntegerField()
    non_peer_review_journals_national = models.IntegerField()
    non_peer_review_journals_others = models.IntegerField()
    e_journals_international = models.IntegerField()
    e_journals_national = models.IntegerField()
    e_journals_others = models.IntegerField()
    conference_proceedings_international = models.IntegerField()
    conference_proceedings_national = models.IntegerField()
    conference_proceedings_others = models.IntegerField()

class Major_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Minor_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Interdisciplinary_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Industry_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class College_sponsored_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Student_research_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Other_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class Total_Projects_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    duration = models.CharField(max_length=150)
    name_of_agency = models.CharField(max_length=200)
    total_grant_sanctioned = models.IntegerField()
    received = models.IntegerField()

class University_department_funds(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    ugc_sap = models.IntegerField()
    cas = models.IntegerField()
    dst_fist = models.IntegerField()
    dpe = models.IntegerField()
    dbt_scheme_funds = models.IntegerField()

class Funds_For_colleges(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    autonomy = models.IntegerField()
    cpe = models.IntegerField()
    dbt_star_scheme = models.IntegerField()
    inspire = models.IntegerField()
    ce = models.IntegerField()
    others = models.IntegerField()

class Conferences_organized_institution(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    number_international = models.IntegerField()
    number_national = models.IntegerField()
    number_state = models.IntegerField()
    number_university = models.IntegerField()
    number_college = models.IntegerField()
    sponsor_international = models.IntegerField()
    sponsor_national = models.IntegerField()
    sponsor_state = models.IntegerField()
    sponsor_university = models.IntegerField()
    sponsor_college = models.IntegerField()

class Patents(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    national_applied = models.IntegerField()
    national_granted = models.IntegerField()
    international_applied = models.IntegerField()
    international_granted = models.IntegerField()
    commercialised_applied = models.IntegerField()
    commercialised_granted = models.IntegerField()

class Awards(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    total = models.IntegerField()
    international = models.IntegerField()
    national = models.IntegerField()
    state = models.IntegerField()
    university = models.IntegerField()
    dist = models.IntegerField()
    college = models.IntegerField()

class NSS_events(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    university = models.IntegerField()
    state = models.IntegerField()
    national = models.IntegerField()
    international = models.IntegerField()

class NCC_events(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    university = models.IntegerField()
    state = models.IntegerField()
    national = models.IntegerField()
    international = models.IntegerField()

class NSS_awards(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    university = models.IntegerField()
    state = models.IntegerField()
    national = models.IntegerField()
    international = models.IntegerField()

class NCC_awards(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    university = models.IntegerField()
    state = models.IntegerField()
    national = models.IntegerField()
    international = models.IntegerField()

class Extension_activities(models.Model):
    Criteria3 = models.ForeignKey(Criteria3, on_delete=models.CASCADE)
    university = models.IntegerField()
    college = models.IntegerField()
    ncc = models.IntegerField()
    nss = models.IntegerField()
    other = models.IntegerField()
