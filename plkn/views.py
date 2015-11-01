from datetime import datetime
import sys
from flask import Blueprint, session, request, url_for, render_template, redirect, jsonify, send_from_directory, current_app, make_response

from file_handler import *
from receipt import *

from user import *
from race import *
from company import *
from religion import *
from education import *
from relation import *
from blood_group import *
from trainee import *
from admittance import *
from inventory import *

general = Blueprint('general', __name__)
webservice = Blueprint('webservice', __name__)

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@general.before_request
def _db_connect():
    database.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@general.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()

@general.route('/')
def Index():
    return render_template('index.html')

@general.route('/Sign-Up', methods=['POST', 'GET'])
def Sign_Up():
    error = ''
    if request.method == 'POST':
        if Register(request.form['full_name'],
                    request.form['email'],
                    request.form['password'],
                    request.form['phone_no']):
            return redirect(url_for(Log_User_In(request.form['email'])))
        else:
            error = 'Email already in use'
    # was GET or the credentials were invalid
    return render_template('sign-up.html', error=error)

@general.route('/Sign-Out')
def Sign_Out():
    session.pop('username', None)
    return render_template('sign-in.html')

@general.route('/Sign-In', methods=['POST', 'GET'])
def Sign_In(error = ''):
    if request.method == 'POST':
        if request.form['email'] and request.form['password']:
            if Authenticate(request.form['email'], request.form['password']):
                return redirect(url_for(Log_User_In(request.form['email'])))
            else:
                error = 'Invalid email or password'
        else:
            error = 'Please enter email and password'
    # was GET or the credentials were invalid
    return render_template('sign-in.html', error=error)

@general.route('/Dashboard')
def Dashboard():
    if 'username' in session:
        return render_template('dashboard.html', user_name=session['username'], level=session['level'])
        #return 'Logged in as %s' % escape(session['username'])
    return redirect(url_for('.Sign_In', error="You are not logged in"))

@general.route('/Operation-Races')
def Race():
    races = Races.select().order_by(Races.id)
    return render_template('race.html', user_name=session['username'], level=session['level'], races = races)

@general.route('/Operation-Races-New', methods=['POST', 'GET'])
def Races_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Race(request.form['name']):
				return redirect(url_for('.Race'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('race-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Operation-Companies')
def Company():
    companies = Companies.select().order_by(Companies.id)
    return render_template('company.html', user_name=session['username'], level=session['level'], companies = companies)

@general.route('/Operation-Companies-New', methods=['POST', 'GET'])
def Company_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Company(request.form['name']):
				return redirect(url_for('.Company'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('company-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Operation-Religions')
def Religion():
    religions = Religions.select().order_by(Religions.id)
    return render_template('religion.html', user_name=session['username'], level=session['level'], religions = religions)

@general.route('/Operation-Religions-New', methods=['POST', 'GET'])
def Religion_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Religion(request.form['name']):
				return redirect(url_for('.Religion'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('religion-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Operation-Educations')
def Education():
    educations = Educations.select().order_by(Educations.id)
    return render_template('education.html', user_name=session['username'], level=session['level'], educations = educations)

@general.route('/Operation-Educations-New', methods=['POST', 'GET'])
def Education_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Education(request.form['name']):
				return redirect(url_for('.Education'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('education-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Operation-Relations')
def Relation():
    relations = Relations.select().order_by(Relations.id)
    return render_template('relation.html', user_name=session['username'], level=session['level'], relations = relations)

@general.route('/Operation-Relations-New', methods=['POST', 'GET'])
def Relation_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Relation(request.form['name']):
				return redirect(url_for('.Relation'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('relation-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Operation-Blood-Groups')
def Blood_Group():
    blood_groups = BloodGroups.select().order_by(BloodGroups.id)
    return render_template('blood-group.html', user_name=session['username'], level=session['level'], blood_groups = blood_groups)

@general.route('/Operation-Blood-Groups-New', methods=['POST', 'GET'])
def Blood_Group_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Blood_Group(request.form['name']):
				return redirect(url_for('.Blood_Group'))
            else:
                error = 'Error Occured, Race Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('blood-group-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Management-Trainees', methods=['POST', 'GET'])
def Trainee():
    if request.method == 'POST':
        page_no = 1
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.ic_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        trainees = []
        
    return render_template('trainee.html', user_name=session['username'], level=session['level'], trainees = trainees, page = page_no)

@general.route('/Management-Trainees-New', methods=['POST', 'GET'])
def Trainee_New():
    error = ''
    races = Races.select().order_by(Races.id)
    companies = Companies.select().order_by(Companies.id)
    religions = Religions.select().order_by(Religions.id)
    educations = Educations.select().order_by(Educations.id)
    relations = Relations.select().order_by(Relations.id)
    if request.method == 'POST':
        if request.form['ic_no']:
            if Create_Trainee(request.form['name'], request.form['ic_no'], request.form['company'], request.form['index_no'], 
                              request.form['blok_no'], request.form['room_no'], request.form['bed_no'], 
                              request.form['gender'], request.form['race'], request.form['religion'], request.form['age'], 
                              request.form['phone1'], request.form['phone2'],
                              request.form['address1'], request.form['address2'], request.form['address3'],
                              request.form['postcode'], request.form['city'], request.form['state'],
                              request.form['is_married'], request.form['education'], request.form['occupation'], request.form['bsn_account_no'],
                              request.form['is_shooter'], request.form['is_left_handed'], request.form['is_registered'], request.form['report_in_date'],
                              request.form['kin_name'], request.form['relation'], request.form['kin_address'], 
                              request.form['kin_phone'], request.form['kin_occupation']):
                return redirect(url_for('.Trainee'))
            else:
                error = 'Error Occured, Trainee Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('trainee-form.html', user_name=session['username'], level=session['level'], races = races, edit = False, delete = False,
                           companies = companies, religions = religions, educations = educations, relations = relations, error=error)

@general.route('/Management-Trainees-Edit', methods=['POST', 'GET'])
def Trainee_Edit():
    error = ''
    races = Races.select().order_by(Races.id)
    companies = Companies.select().order_by(Companies.id)
    religions = Religions.select().order_by(Religions.id)
    educations = Educations.select().order_by(Educations.id)
    relations = Relations.select().order_by(Relations.id)
    if request.method == 'POST':
        if request.form['ic_no']:
            if Update_Trainee(request.form['ic_no'], request.form['name'], request.form['company'], request.form['index_no'], 
                              request.form['blok_no'], request.form['room_no'], request.form['bed_no'], 
                              request.form['gender'], request.form['race'], request.form['religion'], request.form['age'], 
                              request.form['phone1'], request.form['phone2'],
                              request.form['address1'], request.form['address2'], request.form['address3'],
                              request.form['postcode'], request.form['city'], request.form['state'],
                              request.form['is_married'], request.form['education'], request.form['occupation'], request.form['bsn_account_no'],
                              request.form['is_shooter'], request.form['is_left_handed'], request.form['is_registered'], request.form['report_in_date'],
                              request.form['kin_name'], request.form['relation'], request.form['kin_address'], 
                              request.form['kin_phone'], request.form['kin_occupation']):
                #return redirect(url_for('.Trainee'))
                error = "Trainee Updated!"
            else:
                error = 'Error Updating Trainee Info'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    if request.method == 'POST':
        ic_no = request.form['ic_no']
    else:
        ic_no = request.args.get('ic_no')
    trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
    return render_template('trainee-form.html', user_name=session['username'], level=session['level'], trainee = trainee, races = races, edit = True,
                           delete = False, companies = companies, religions = religions, educations = educations, relations = relations, error=error)

@general.route('/Management-Trainees-Delete', methods=['POST', 'GET'])
def Trainee_Delete():
    error = ''
    races = Races.select().order_by(Races.id)
    companies = Companies.select().order_by(Companies.id)
    religions = Religions.select().order_by(Religions.id)
    educations = Educations.select().order_by(Educations.id)
    relations = Relations.select().order_by(Relations.id)
    if request.method == 'POST':
        if request.form['ic_no']:
            if Delete_Trainee(request.form['ic_no']):
                return redirect(url_for('.Trainee'))
            else:
                error = 'Error Deleting Trainee Info'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    if request.method == 'POST':
        ic_no = request.form['ic_no']
    else:
        ic_no = request.args.get('ic_no')
    trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
    return render_template('trainee-form.html', user_name=session['username'], level=session['level'], trainee = trainee, races = races, edit = True,
                           delete = True, companies = companies, religions = religions, educations = educations, relations = relations, error=error)

@general.route('/Management-Healths', methods=['POST', 'GET'])
def Trainee_Health():
    if request.method == 'POST':
        page_no = 1
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        trainees = Trainees.select().where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    return render_template('trainee-health.html', user_name=session['username'], level=session['level'], trainees = trainees, page = page_no)

@general.route('/Management-Healths-Edit', methods=['POST', 'GET'])
def Trainee_Health_Edit():
    error = ''
    races = Races.select().order_by(Races.id)
    companies = Companies.select().order_by(Companies.id)
    religions = Religions.select().order_by(Religions.id)
    educations = Educations.select().order_by(Educations.id)
    relations = Relations.select().order_by(Relations.id)
    blood_groups = BloodGroups.select().order_by(BloodGroups.id)
    if request.method == 'POST':
        if request.form['ic_no']:
            ic_no = request.form['ic_no']
            if Update_Health(request.form['ic_no'], request.form['blood_group'], request.form['height'], 
                             request.form['weight'], request.form['bmi'], request.form['is_allergic'] , 
                             request.form['allergies'] , request.form['is_food_intolerant'],
                             request.form['food_intolerance'], request.form['reference_no'], request.form['is_declared'],
                             request.form['medicine_journal']):
				#return redirect(url_for('.Trainee_Health'))
                error = "Health Updated!"
            else:
                error = 'Error Updating Trainee Health'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    if request.method == 'GET':
        ic_no = request.args.get('ic_no')
    trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
    return render_template('trainee-health-form.html', user_name=session['username'], level=session['level'], trainee = trainee, races = races, 
                           companies = companies, religions = religions, educations = educations, relations = relations, blood_groups = blood_groups,
                           error=error)

@general.route('/Management-Admittances', methods=['POST', 'GET'])
def Trainee_Admittance():    
    if request.method == 'POST':
        page_no = 1
        admittances = Admittances.select().join(Trainees).where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Admittances.id).paginate(page_no, 10)
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        admittances = []
        trainees = []

    return render_template('trainee-admittance.html', user_name=session['username'], level=session['level'], admittances = admittances, trainees = trainees, page = page_no)

@general.route('/Management-Admittances-New', methods=['POST', 'GET'])
def Trainee_Admittance_New():
    error = ''
    if request.method == 'POST':
        if request.form['ic_no']:
            if Create_Admittance(request.form['ic_no'], request.form['details'], request.form['diagnosis'], 
                              request.form['blood_pressure'], request.form['temperature'], request.form['pulse'],
                              request.form['respiration']):
                return redirect(url_for('.Trainee_Admittance'))
            else:
                error = 'Error Occured, Trainee Admittance Already Exist'
        else:
            error = 'Please Enter All Values'
    else:
        # was GET or error occurred
        if request.method == 'GET':
            ic_no = request.args.get('ic_no')
        trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
        admittance = []
    return render_template('trainee-admittance-form.html', user_name=session['username'], level=session['level'], trainee = trainee,
                           admittance = admittance, edit = False, delete = False, error=error)

@general.route('/Management-Admittances-Edit', methods=['POST', 'GET'])
def Trainee_Admittance_Edit():
    error = ''
    if request.method == 'POST':
        if request.form['admittance_id']:
            admittance_id = request.form['admittance_id']
            if Update_Admittance(request.form['admittance_id'], request.form['details'], request.form['diagnosis'], 
                              request.form['blood_pressure'], request.form['temperature'], request.form['pulse'],
                              request.form['respiration']):
                #return redirect(url_for('.Trainee_Admittance'))
                error = "Admittance Updated!"
            else:
                error = 'Error Occured, Trainee Admittance Already Exist'
        else:
            error = 'Please Enter All Values'
    else:
        # was GET or error occurred
        if request.method == 'GET':
            admittance_id = request.args.get('id')
    admittance = Admittances.select().where(Admittances.id==admittance_id).get()
    companies = Companies.select().order_by(Companies.id)
    trainee = Trainees.select().where(Trainees.ic_no==admittance.trainee.ic_no).get()
    return render_template('trainee-admittance-form.html', user_name=session['username'], level=session['level'], trainee = trainee, companies = companies,
                           admittance = admittance, edit = True, delete = False, error=error)

@general.route('/Management-Admittances-Report', methods=['POST', 'GET'])
def Trainee_Admittance_Report():
    if request.method == 'POST':
        page_no = 1
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        trainees = Trainees.select().where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    return render_template('trainee-admittance-report.html', user_name=session['username'], level=session['level'], trainees = trainees, page = page_no)

@general.route('/Management-Logistics', methods=['POST', 'GET'])
def Trainee_Logistic():
    if request.method == 'POST':
        page_no = 1
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        trainees = Trainees.select().where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    return render_template('trainee-logistic.html', user_name=session['username'], level=session['level'], trainees = trainees, page = page_no)

@general.route('/Management-Logistics-Print', methods=['POST', 'GET'])
def Trainee_Logistic_Print():
    if request.method == 'POST':
        page_no = 1
        trainees = Trainees.select().where(Trainees.name.contains(request.form['search']) | Trainees.index_no.contains(request.form['search'])).where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    else:
        if request.args.get('pageno'):
            page_no = int(request.args.get('pageno'))
        else:
            page_no = 1
        trainees = Trainees.select().where(Trainees.is_deleted==False).order_by(Trainees.id).paginate(page_no, 10)
    return render_template('trainee-logistic-print.html', user_name=session['username'], level=session['level'], trainees = trainees, page = page_no)

@general.route('/Management-Logistics-Edit', methods=['POST', 'GET'])
def Trainee_Logistic_Edit():
    error = ''
    races = Races.select().order_by(Races.id)
    companies = Companies.select().order_by(Companies.id)
    religions = Religions.select().order_by(Religions.id)
    educations = Educations.select().order_by(Educations.id)
    relations = Relations.select().order_by(Relations.id)
    
    shirt_sizes = ShirtSizes.select().order_by(ShirtSizes.id)
    pant_sizes = PantSizes.select().order_by(PantSizes.id)
    shoe_sizes = ShoeSizes.select().order_by(ShoeSizes.id)
    free_sizes = FreeSizes.select().order_by(FreeSizes.id)
    beret_sizes = BeretSizes.select().order_by(BeretSizes.id)
    if request.method == 'POST':
        if request.form['ic_no']:
            ic_no = request.form['ic_no']
            """
            if Update_Logistic(request.form['ic_no'], request.form['shirt_class_male'], request.form['shirt_class_female'], 
                               request.form['shirt_sport_male'], request.form['shirt_sport_female'], request.form['inner_male'],
                               request.form['inner_female'], request.form['shoe_class_male'], request.form['shoe_class_female'],
                               request.form['shirt_celoreng'], request.form['track_bottom_black'], request.form['shoe_sport'],
                               request.form['pants_celoreng'], request.form['pants_class'], request.form['shoe_spike'],
                               request.form['beret']):
				#return redirect(url_for('.Trainee_Logistic'))
                error = "Logistic Updated!"
            else:
                error = 'Error Updating Trainee Logistic'
            """
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    if request.method == 'GET':
        ic_no = request.args.get('ic_no')
    trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
    return render_template('trainee-logistic-form.html', user_name=session['username'], level=session['level'], trainee = trainee, races = races, 
                           companies = companies, religions = religions, educations = educations, relations = relations, 
                           shirt_sizes = shirt_sizes, pant_sizes = pant_sizes, shoe_sizes = shoe_sizes, free_sizes = free_sizes, beret_sizes = beret_sizes,
                           error=error)

@general.route('/Management-Inventory-Categories')
def Inventory_Category():
    categories = InventoryCategories.select().order_by(InventoryCategories.id)
    return render_template('inventory-category.html', user_name=session['username'], level=session['level'], categories = categories)

@general.route('/Management-Inventory-Categories-New', methods=['POST', 'GET'])
def Inventory_Category_New():
    error = ''
    if request.method == 'POST':
        if request.form['name']:
            if Create_Inventory_Category(request.form['name']):
                return redirect(url_for('.Inventory_Category'))
            else:
                error = 'Error Occured, Category Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    return render_template('inventory-category-form.html', user_name=session['username'], level=session['level'], error=error)

@general.route('/Management-Inventories')
def Inventory():
    inventories = Inventories.select().order_by(Inventories.id)
    return render_template('inventory.html', user_name=session['username'], level=session['level'], inventories = inventories)

@general.route('/Management-Inventories-New', methods=['POST', 'GET'])
def Inventory_New():
    error = ''
    if request.method == 'POST':
        if request.form['item']:
            if Create_Inventory(request.form['item'], request.form['category'], request.form['code'], request.form['unit_price']):
                return redirect(url_for('.Inventory'))
            else:
                error = 'Error Occured, Inventory Already Exist'
        else:
            error = 'Please Enter All Values'
    # was GET or error occurred
    categories = InventoryCategories.select().order_by(InventoryCategories.id)
    return render_template('inventory-form.html', user_name=session['username'], level=session['level'], categories = categories, edit = False, error=error)

#------ REPORTS REPORTS REPORTS REPORTS  ------------------------------------------------------------------------------

@general.route('/Report-Trainees')
def Report_Trainee():
    report_type = request.args.get('type')
    if report_type == "bsn_account":
        trainees = Trainees.select().where(Trainees.is_deleted==False).where(Trainees.bsn_account_no!="").order_by(Trainees.bsn_account_no)
        items = []
        report_view = "list"
    elif report_type == "medical":
        trainees = Trainees.select().where(Trainees.is_deleted==False)
        admittances = Admittances.select().where(Admittances.is_deleted==False)
        items = admittances
        report_view = "list"
    elif report_type == "allergic":
        trainees = Trainees.select().where(Trainees.is_deleted==False).where(Trainees.is_allergic==True).order_by(Trainees.is_allergic)
        items = []
        report_view = "list"
    elif report_type == "is_registered":
        trainees = Trainees.select().where(Trainees.is_deleted==False)
        registered = 0
        unregistered = 0
        for trainee in trainees:
            if trainee.is_registered==True:
                registered += 1
            else:
                unregistered += 1
        items = []
        items.append("registered:"+str(registered))
        items.append("unregistered:"+str(unregistered))
        report_view = "pie"
    elif report_type == "gender":
        trainees = Trainees.select().where(Trainees.is_deleted==False)
        male = 0
        female = 0
        for trainee in trainees:
            if trainee.gender=="Male":
                male += 1
            else:
                female += 1
                
        items = []
        items.append("male:"+str(male))
        items.append("female:"+str(female))
        report_view = "pie"
    elif report_type == "race":
        trainees = Trainees.select().where(Trainees.is_deleted==False)
        races = Races.select().where(Races.is_deleted==False)
        
        trainee_race = [0 for x in range(races.count())] 
        
        for trainee in trainees:
            trainee_race[trainee.race.id-1] += 1
            
        items = []
        for item in races:
            items.append(item.name + ":"+ str(trainee_race[item.id-1]))
        report_view = "pie"
    elif report_type == "religion":
        trainees = Trainees.select().where(Trainees.is_deleted==False)
        religions = Religions.select().where(Religions.is_deleted==False)
        
        trainee_religion = [0 for x in range(religions.count())] 
        
        for trainee in trainees:
            trainee_religion[trainee.religion.id-1] += 1
            
        items = []
        for item in religions:
            items.append(item.name + ":"+ str(trainee_religion[item.id-1]))
        report_view = "pie"
    else:
        trainees = Trainees.select().where(Trainees.is_deleted==False).order_by(Trainees.id)
        items = []
        report_view = "list"
    
    if report_view == "list":
        return render_template('report_list.html', user_name=session['username'], level=session['level'], report_type = report_type, trainees = trainees, items = items, admittances = admittances)
    elif report_view == "bar":
        return render_template('report_bar.html', user_name=session['username'], level=session['level'], report_type = report_type, items = items)
    else: #pie
        return render_template('report_pie.html', user_name=session['username'], level=session['level'], report_type = report_type, items = items)

@general.route('/Print-Trainees-Logistic')
def Print_Logistic():
    ic_no = request.args.get('ic_no')
    new_print = LastPrintCount.select().where(LastPrintCount.id==1).get()
    new_print.no = new_print.no + 1
    print_id = new_print.no
    new_print.save()
    trainees = Trainees.select().where(Trainees.ic_no==ic_no).where(Trainees.is_deleted==False).order_by(Trainees.id)
    return render_template('logistic-print.html', user_name=session['username'], level=session['level'], print_id = print_id, trainees = trainees)

@general.route('/Print-Admittances')
def Print_Medical():
    admittance_id = request.args.get('id')
    admittance = Admittances.select().where(Admittances.id==admittance_id).get()
    companies = Companies.select().order_by(Companies.id)
    return render_template('medical-print.html', user_name=session['username'], level=session['level'], admittance = admittance, companies = companies)

@general.route('/Print-Trainee-Admittances')
def Print_Admittances():
    ic_no = request.args.get('ic_no')
    trainees = Trainees.select().where(Trainees.ic_no==ic_no).where(Trainees.is_deleted==False)
    admittances = Admittances.select().join(Trainees).where(Trainees.ic_no==ic_no).where(Trainees.is_deleted==False)
    return render_template('admittances-print.html', user_name=session['username'], level=session['level'], admittances = admittances, trainees = trainees)
#------ Web SERVICES  --------------------------

@webservice.route('/User/<email>')
def User_Get(email):
    user = Users.get_by_id(email)
    # was GET or error occurred
    return jsonify(email=email, name=user.full_name, phone=user.phone_no, level=user.level)

@webservice.route('/EmployeeType/<type_name>')
def Employee_Type_Get():
    employee_type = EmployeeTypes.get_by_id(type_name)
    # was GET or error occurred
    return jsonify(employee_type)

"""
@general.route('/Print_Receipt')
def Print_Receipt():
    order_no = request.args.get('order_no')
    
    order = Orders.select().where(Orders.no==order_no).get()
    order_items = Order_Items.select().where(Order_Items.order==order)
    
    if order and order_items:
        import StringIO
        output = StringIO.StringIO()
        make_receipt(order, order_items, output)
        
        pdf_out = output.getvalue()
        output.close()

        response = make_response(pdf_out)
        #response.headers['Content-Disposition'] = "attachment; filename='sakulaci.pdf"
        response.mimetype = 'application/pdf'
        #os.path.join(current_app.config.get('PRINT_FOLDER'), response)
        return response
    return redirect(url_for('.Waiter'))
"""
