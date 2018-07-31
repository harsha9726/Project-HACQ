from django.shortcuts import render,get_object_or_404,redirect
from . import forms as f
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models as m
# Create your views here.

def index(request):
    return render(request, 'form/home.html')

def institute_fill(request):
    form=f.InstituteForm()
    cycle1=f.Cycle1Form()
    cycle2=f.Cycle2Form()
    cycle3=f.Cycle3Form()
    cycle4=f.Cycle4Form()
    special_status=f.Special_statusForm()
    iqac_composition_activities=f.IQAC_composition_activitiesForm()
    stakeholders_meetings = f.Stakeholders_meetingsForm()
    seminars_conferences = f.Seminars_conferencesForm()
    forms = {'form':form, 'cycle1':cycle1, 'cycle2':cycle2, 'cycle3': cycle3, 'cycle4' : cycle4,
    'special_status': special_status, 'iqac_composition_activities': iqac_composition_activities,
    'stakeholders_meetings': stakeholders_meetings, 'seminars_conferences':seminars_conferences }
    return render(request,'form\institution Details 1.html',forms)

def Criteria2_fill(request):
    return render(request, 'form/Criteria2.html')

def Criteria4_fill(request):
    return render(request, 'form/Criteria4.html')

def Criteria6_fill(request):
    return render(request, 'form/Criteria6.html')

def Criteria7_fill(request):
    return render(request, 'form/Criteria7.html')

def form_details(request):
    form=m.Institute.objects.order_by('-pk')
    context ={'form1': form }
    return render(request, 'form/list.html',context)

def save_institution_details(request):
    if request.method == 'POST':
        form=f.InstituteForm(request.POST)
        if form.is_valid():# and cycle1.is_valid() and cycle2.is_valid() and cycle3.is_valid() and cycle4.is_valid():
            new_institute = m.Institute(name = request.POST.get('name'),
                                        address_line_1=request.POST.get('address_line_1'),
                                        address_line_2=request.POST.get('address_line_2'),
                                        city=request.POST.get('city'),
                                        state=request.POST.get('state'),
                                        pincode=request.POST.get('pincode'),
                                        college_email_address=request.POST.get('college_email_address'),
                                        college_contact_no=request.POST.get('college_contact_no'),
                                        head_of_institute=request.POST.get('head_of_institute'),
                                        telephone=request.POST.get('telephone'),
                                        college_mobile=request.POST.get('college_mobile'),
                                        iqac_coordinator=request.POST.get('iqac_coordinator'),
                                        coordinator_mobile=request.POST.get('coordinator_mobile'),
                                        iqac_email=request.POST.get('iqac_email'),
                                        naac_track_id=request.POST.get('naac_track_id'),
                                        naac_executive_committe_date=request.POST.get('naac_executive_committe_date'),
                                        college_website = request.POST.get('college_website'),
                                        aqar_weblink = request.POST.get('aqar_weblink'),
                                        date_of_iqac_establishment = request.POST.get('date_of_iqac_establishment'),
                                        aqar_for_year =request.POST.get('aqar_for_year'),
                                        aqar_submission_1 = request.POST.get('aqar_submission_1'),
                                        aqar_submission_2 = request.POST.get('aqar_submission_2'),
                                        aqar_submission_3 = request.POST.get('aqar_submission_3'),
                                        aqar_submission_4 = request.POST.get('aqar_submission_4'),
                                        university = request.POST.get('university'),
                                        Affiliated= request.POST.get('Affiliated'),
                                        Constituent = request.POST.get('Constituent'),
                                        autonomous = request.POST.get('autonomous'),
                                        regulatory_agency_approved = request.POST.get('regulatory_agency_approved'),
                                        type_of_institution = request.POST.get('type_of_institution'),
                                        financial_status = request.POST.get('financial_status'),
                                        type_of_faculty = request.POST.get('type_of_faculty'),
                                        type_of_faculty_others = request.POST.get('type_of_faculty_others'),
                                        affiliating_university = request.POST.get('affiliating_university'),
                                        iqac_funding = request.POST.get('iqac_funding'),
                                        iqac_funding_amount = request.POST.get('iqac_funding_amount'))
            new_cycle1 = m.Cycle1(grade = request.POST.get('grade'),
                                    cgpa= request.POST.get('cgpa'),
                                    year_of_accreditation=request.POST.get('year_of_accreditation'),
                                    validity_period=request.POST.get('validity_period'))
            new_cycle2 = m.Cycle2(grade = request.POST.get('grade'),
                                    cgpa= request.POST.get('cgpa'),
                                    year_of_accreditation=request.POST.get('year_of_accreditation'),
                                    validity_period=request.POST.get('validity_period'))
            new_cycle3 = m.Cycle3(grade = request.POST.get('grade'),
                                    cgpa= request.POST.get('cgpa'),
                                    year_of_accreditation=request.POST.get('year_of_accreditation'),
                                    validity_period=request.POST.get('validity_period'))
            new_cycle4 = m.Cycle4(grade = request.POST.get('grade'),
                                    cgpa= request.POST.get('cgpa'),
                                    year_of_accreditation=request.POST.get('year_of_accreditation'),
                                    validity_period=request.POST.get('validity_period'))
            new_iqac_composition_activities =m.IQAC_composition_activities(teachers = request.POST.get('teachers'),
                                                                            administrative_staff = request.POST.get('administrative_staff'),
                                                                            students = request.POST.get('students'),
                                                                            management_representatives = request.POST.get('management_representatives'),
                                                                            alumni = request.POST.get('alumni'),
                                                                            stakeholder_community_representatives = request.POST.get('stakeholder_community_representatives'),
                                                                            employers_industrialists = request.POST.get('employers_industrialists'),
                                                                            external_experts = request.POST.get('external_experts'),
                                                                            total_members = request.POST.get('total_members'),
                                                                            iqac_meetings_held = request.POST.get('iqac_meetings_held'),
                                                                            funding_received = request.POST.get('funding_received'),
                                                                            funding_amount = request.POST.get('funding_amount'),
                                                                            activites_contributions = request.POST.get('activites_contributions'),
                                                                            plan_of_action = request.POST.get('plan_of_action'),
                                                                            achivements_by_year = request.POST.get('achivements_by_year'),
                                                                            aqar_statutory_body = request.POST.get('aqar_statutory_body'),
                                                                            aqar_statutory_body_yes = request.POST.get('aqar_statutory_body_yes'),
                                                                            plan_of_action_taken = request.POST.get('plan_of_action_taken'))
            new_stakeholders_meentings = m.Stakeholders_meetings(total = request.POST.get('total'),
                                                                faculty = request.POST.get('faculty'),
                                                                nonteaching_staff_students = request.POST.get('nonteaching_staff_students'),
                                                                alumni = request.POST.get('alumni'),
                                                                others = request.POST.get('others'))
            new_seminars_conferences = m.Seminars_conferences(total = request.POST.get('total'),
                                                                international = request.POST.get('international'),
                                                                national = request.POST.get('national'),
                                                                state = request.POST.get('state'),
                                                                institute = request.POST.get('institute'),
                                                                themes = request.POST.get('themes'))
            new_institute.save()
            new_cycle1.save()
            new_cycle2.save()
            new_cycle3.save()
            new_cycle4.save()
            new_iqac_composition_activities.save()
            new_stakeholders_meentings.save()
            new_seminars_conferences.save()
            return redirect('details')
        else:
            return render(request,'form/start.html')
