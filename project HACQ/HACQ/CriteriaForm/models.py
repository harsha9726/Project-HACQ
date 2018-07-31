from django.db import models
from datetime import datetime


# Create your models here.

class Form(models.Model):
    create_date = models.DateTimeField('date created',auto_now_add=True,blank=True)

                #===========Institutional Details models===========#

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



                        #=============Criteria 1 models==================#

'''
class PhD(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class PG(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class UG(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class PG_Dimploma(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Advanced_Dimploma(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Diploma(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Certificate(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Others(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Interdisciplinary(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()

class Innovative(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    Number_of_existing_programmes = models.IntegerField()
    Number_of_programmes_added_during_year = models.IntegerField()
    Number_of_self_financing_programmes = models.IntegerField()
    Number_of_value_added_career_Oriented_programmes = models.IntegerField()
'''
