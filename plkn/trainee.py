from flask import session
from models import *

def Create_Trainee(new_name, new_ic_no, new_company_id, new_index_no, #new_blok_no,
                   new_room_no, new_bed_no, new_gender, new_race_id, new_religion_id, new_age, new_phone1, new_phone2,
                   new_address1, new_address2, new_address3, new_postcode, new_city, new_state,
                   new_is_married, new_education_id, new_occupation, new_bsn_account_no, new_is_shooter,
                   new_is_left_handed, new_is_registered, new_report_in_date,
                   new_kin_name, new_relation_id, new_kin_address, new_kin_phone, new_kin_occupation):
    try:
        new_trainee = Trainees.select().where(Trainees.ic_no==new_ic_no).get()
    except Trainees.DoesNotExist:
        if new_gender != "" and new_race_id != "":
            #filled gender, & race
            #########  RULES SET HERE ##############################################################3
            #set index no based on gender
            new_index = LastIndex.select().where(LastIndex.id==1).get()
            if new_gender == "Male":
                new_index.male = new_index.male + 2
            else:
                new_index.female = new_index.female + 2
                
            #set company, bed & room no based on race
            group = GroupPlacement.select().where(GroupPlacement.race==new_race_id).get()
            if group.alpha == 0:
                group.alpha = 1
                #put into alpha
                company_placed = Companies.select().where(Companies.name=="Alpha").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL1").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL2").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP7").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP8").get()
                        dorm.occupancy = dorm.occupancy + 1
            elif group.bravo == 0:
                group.bravo = 1
                #put into bravo
                company_placed = Companies.select().where(Companies.name=="Bravo").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL3").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL4").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP5").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP6").get()
                        dorm.occupancy = dorm.occupancy + 1
            elif group.charlie == 0:
                group.charlie = 1
                #put into charlie
                company_placed = Companies.select().where(Companies.name=="Charlie").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL5").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL6").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP3").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP6A").get()
                        dorm.occupancy = dorm.occupancy + 1
            else:
                group.alpha = 0
                group.bravo = 0
                group.charlie = 0
                #put into delta
                company_placed = Companies.select().where(Companies.name=="Delta").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL7").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL8").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP2").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP5A").get()
                        dorm.occupancy = dorm.occupancy + 1
            #########  RULES SET HERE ##############################################################

        new_trainee = Trainees.create(name = new_name, 
                                      ic_no = new_ic_no,
                                      company = None if new_race_id == "" else company_placed,
                                      index_no = "" if new_gender == "" else "SW151" + '{:0>3}'.format(str(new_index.male if new_gender == "Male" else new_index.female)),
                                      #blok_no = new_blok_no,
                                      room_no = "" if new_race_id == "" else dorm.room_no,
                                      bed_no = "" if new_race_id == "" else dorm.occupancy,
                                      gender = None if new_gender == "" else new_gender,
                                      race = None if new_race_id == "" else Races.select().where(Races.id==new_race_id).get(),
                                      religion = None if new_religion_id == "" else Religions.select().where(Religions.id==new_religion_id).get(),
                                      age = new_age,
                                      phone1 = new_phone1,
                                      phone2 = new_phone2,
                                      address1 = new_address1,
                                      address2 = new_address2,
                                      address3 = new_address3,
                                      postcode = new_postcode,
                                      city = new_city,
                                      state = new_state,
                                      is_married = True if new_is_married == "True" else False,
                                      education = Educations.select().where(Educations.id==new_education_id).get(),
                                      occupation = new_occupation,
                                      bsn_account_no = new_bsn_account_no,
                                      is_shooter = True if new_is_shooter == "True" else False,
                                      is_left_handed = True if new_is_left_handed == "True" else False,
                                      is_registered = True if new_is_registered == "True" else False,
                                      report_in_date = new_report_in_date,
                                      kin_name = new_kin_name,
                                      relation = Relations.select().where(Relations.id==new_relation_id).get(),
                                      kin_address = str(new_kin_address),
                                      kin_phone = new_kin_phone,
                                      kin_occupation = new_kin_occupation,
                                      created_by = Users.select().where(Users.email==session['email']).get())
        if not new_gender == "": new_index.save()
        if not new_race_id == "": 
            group.save()
            dorm.save()
        return True
    else:
        return False

def Update_Trainee(ic_no, new_name, new_company_id, new_index_no, #new_blok_no,
                   new_room_no, new_bed_no, new_gender, new_race_id, new_religion_id, new_age, new_phone1, new_phone2,
                   new_address1, new_address2, new_address3, new_postcode, new_city, new_state,
                   new_is_married, new_education_id, new_occupation, new_bsn_account_no, new_is_shooter,
                   new_is_left_handed, new_is_registered, new_report_in_date,
                   new_kin_name, new_relation_id, new_kin_address, new_kin_phone, new_kin_occupation):
    try:
        update_trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
        if update_trainee.index_no == "" and new_gender != "" and new_race_id != "":
            #filled gender, & race
            #########  RULES SET HERE ##############################################################3
            #set index no based on gender
            new_index = LastIndex.select().where(LastIndex.id==1).get()
            if new_gender == "Male":
                new_index.male = new_index.male + 2
            else:
                new_index.female = new_index.female + 2
                
            #set company, bed & room no based on race
            group = GroupPlacement.select().where(GroupPlacement.race==new_race_id).get()
            if group.alpha == 0:
                group.alpha = 1
                #put into alpha
                company_placed = Companies.select().where(Companies.name=="Alpha").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL1").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL2").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP7").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP8").get()
                        dorm.occupancy = dorm.occupancy + 1
            elif group.bravo == 0:
                group.bravo = 1
                #put into bravo
                company_placed = Companies.select().where(Companies.name=="Bravo").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL3").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL4").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP5").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP6").get()
                        dorm.occupancy = dorm.occupancy + 1
            elif group.charlie == 0:
                group.charlie = 1
                #put into charlie
                company_placed = Companies.select().where(Companies.name=="Charlie").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL5").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL6").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP3").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP6A").get()
                        dorm.occupancy = dorm.occupancy + 1
            else:
                group.alpha = 0
                group.bravo = 0
                group.charlie = 0
                #put into delta
                company_placed = Companies.select().where(Companies.name=="Delta").get()
                #put into room--------------------------------------
                if new_gender == "Male":
                    dorm = Dormitory.select().where(Dormitory.room_no=="BL7").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BL8").get()
                        dorm.occupancy = dorm.occupancy + 1
                else:
                    dorm = Dormitory.select().where(Dormitory.room_no=="BP2").get()
                    if dorm.occupancy < 25:
                        dorm.occupancy = dorm.occupancy + 1
                    else:
                        dorm = Dormitory.select().where(Dormitory.room_no=="BP5A").get()
                        dorm.occupancy = dorm.occupancy + 1
            #########  RULES SET HERE ##############################################################
            update_trainee.company = company_placed
            update_trainee.index_no = "SW151" + '{:0>3}'.format(str(new_index.male if new_gender == "Male" else new_index.female))
            update_trainee.room_no = dorm.room_no
            update_trainee.bed_no = dorm.occupancy
        else:
            update_trainee.company = None if new_company_id == "" else Companies.select().where(Companies.id==new_company_id).get()
            update_trainee.index_no = new_index_no
            update_trainee.room_no = new_room_no
            update_trainee.bed_no = new_bed_no

        update_trainee.name = new_name
        #update_trainee.blok_no = new_blok_no
        update_trainee.gender = new_gender
        update_trainee.race = None if new_race_id == "" else Races.select().where(Races.id==new_race_id).get()
        update_trainee.religion = None if new_religion_id == "" else Religions.select().where(Religions.id==new_religion_id).get()
        update_trainee.age = new_age
        update_trainee.phone1 = new_phone1
        update_trainee.phone2 = new_phone2
        update_trainee.address1 = new_address1
        update_trainee.address2 = new_address2
        update_trainee.address3 = new_address3
        update_trainee.postcode = new_postcode
        update_trainee.city = new_city
        update_trainee.state = new_state
        update_trainee.is_married = True if new_is_married == "True" else False
        update_trainee.education = Educations.select().where(Educations.id==new_education_id).get()
        update_trainee.occupation = new_occupation
        update_trainee.bsn_account_no = new_bsn_account_no
        update_trainee.is_shooter = True if new_is_shooter == "True" else False
        update_trainee.is_left_handed = True if new_is_left_handed == "True" else False
        update_trainee.is_registered = True if new_is_registered == "True" else False
        update_trainee.report_in_date = new_report_in_date
        update_trainee.kin_name = new_kin_name
        update_trainee.relation = Relations.select().where(Relations.id==new_relation_id).get()
        update_trainee.kin_address = new_kin_address
        update_trainee.kin_phone = new_kin_phone
        update_trainee.kin_occupation = new_kin_occupation
        update_trainee.created_by = Users.select().where(Users.email==session['email']).get()
        update_trainee.save()
        
        if update_trainee.index_no == "" and new_gender != "" and new_race_id != "":
            new_index.save()
            group.save()
            dorm.save()
        return True
    except Trainees.DoesNotExist:
        return False
    else:
        return False

def Delete_Trainee(ic_no):
    try:
        delete_trainee = Trainees.select().where(Trainees.ic_no==ic_no).get()
        delete_trainee.is_deleted = True
        delete_trainee.created_by = Users.select().where(Users.email==session['email']).get()
        delete_trainee.save()
        return True
    except Trainees.DoesNotExist:
        return False
    else:
        return False

def Update_Health(ic_no, new_blood_group, new_height, new_weight, new_bmi, new_is_allergic, new_allergies, new_is_food_intolerant,
                  new_food_intolerance, new_reference_no, new_is_declared, new_medicine_journal):
    try:
        trainee_health = Trainees.select().where(Trainees.ic_no==ic_no).get()
        trainee_health.blood_group = new_blood_group
        trainee_health.height = new_height
        trainee_health.weight = new_weight
        trainee_health.bmi = new_bmi
        trainee_health.is_allergic = True if new_is_allergic == "True" else False
        trainee_health.allergies = new_allergies
        trainee_health.is_food_intolerant = True if new_is_food_intolerant == "True" else False
        trainee_health.food_intolerance = new_food_intolerance
        trainee_health.reference_no = new_reference_no
        trainee_health.is_declared = (True if new_is_declared == "True" else False)
        trainee_health.medicine_journal = new_medicine_journal
        trainee_health.created_by = Users.select().where(Users.email==session['email']).get()
        trainee_health.save()
        return True
    except Trainees.DoesNotExist:
        return False
    else:
        return False

def Update_Logistic(ic_no, new_shirt_class_male, new_shirt_class_female, new_shirt_sport_male, new_shirt_sport_female, 
                    new_inner_male, new_inner_female, new_shoe_class_male, new_shoe_class_female, new_shirt_celoreng, 
                    new_track_bottom_black, new_shoe_sport, new_pants_celoreng, new_pants_class, new_shoe_spike, new_beret):
    try:
        trainee_logistic = Trainees.select().where(Trainees.ic_no==ic_no).get()
        trainee_logistic.shirt_class_male = new_shirt_class_male
        trainee_logistic.shirt_class_female = new_shirt_class_female
        trainee_logistic.shirt_sport_male = new_shirt_sport_male
        trainee_logistic.shirt_sport_female = new_shirt_sport_female
        trainee_logistic.inner_male = new_inner_male
        trainee_logistic.inner_female = new_inner_female
        trainee_logistic.shoe_class_male = new_shoe_class_male
        trainee_logistic.shoe_class_female = new_shoe_class_female
        trainee_logistic.shirt_celoreng = new_shirt_celoreng
        trainee_logistic.track_bottom_black = new_track_bottom_black
        trainee_logistic.shoe_sport = new_shoe_sport
        trainee_logistic.pants_celoreng = new_pants_celoreng
        trainee_logistic.pants_class = new_pants_class
        trainee_logistic.shoe_spike = new_shoe_spike
        trainee_logistic.beret = new_beret
        trainee_logistic.created_by = Users.select().where(Users.email==session['email']).get()
        trainee_logistic.save()
        return True
    except Trainees.DoesNotExist:
        return False
    else:
        return False