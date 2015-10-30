from flask import session
from models import *

def Create_Admittance(trainee_ic_no, new_details, new_diagnosis, new_blood_pressure, new_temperature, new_pulse, new_respiration):
    try:
        new_admittance = Admittances.create(trainee = Trainees.select().where(Trainees.ic_no==trainee_ic_no).get(),
                                           details = new_details,
                                           diagnosis = new_diagnosis,
                                           blood_pressure = new_blood_pressure,
                                           temperature = new_temperature,
                                           pulse = new_pulse,
                                           respiration = new_respiration,
                                           created_by = Users.select().where(Users.email==session['email']).get())       
        return True
    except Admittances.DoesNotExist:
        return False
    else:
        return False

def Update_Admittance(admittance_id, new_details, new_diagnosis, new_blood_pressure, new_temperature, new_pulse, new_respiration):
    try:
        update_admittance = Admittances.select().where(Admittances.id==admittance_id).get()
        update_admittance.details = new_details
        update_admittance.diagnosis = new_diagnosis
        update_admittance.blood_pressure = new_blood_pressure
        update_admittance.temperature = new_temperature
        update_admittance.pulse = new_pulse
        update_admittance.respiration = new_respiration
        update_admittance.is_deleted = True
        update_admittance.created_by = Users.select().where(Users.email==session['email']).get()
        update_admittance.save()
        return True
    except Admittances.DoesNotExist:
        return False
    else:
        return False

def Delete_Admittance(admittance_id):
    try:
        delete_admittance = Admittances.select().where(Admittances.id==admittance_id).get()
        delete_admittance.is_deleted = True
        delete_admittance.created_by = Users.select().where(Users.email==session['email']).get()
        delete_admittance.save()
        return True
    except Admittances.DoesNotExist:
        return False
    else:
        return False